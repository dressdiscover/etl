import re
from pprint import pprint
from typing import Dict, List, Tuple

from paradicms_etl.models.collection import Collection
from paradicms_etl.models.image import Image
from paradicms_etl.models.institution import Institution
from paradicms_etl.models.work import Work
from paradicms_etl.models.property import Property
from paradicms_etl.models.property_definitions import PropertyDefinitions
from paradicms_etl.models.rights import Rights
from paradicms_etl.transformers._airtable_transformer import _AirtableTransformer
from rdflib import URIRef


class VraCamsTransformer(_AirtableTransformer):
    def transform(self, *, records_by_table, **kwds):
        yield from PropertyDefinitions.as_tuple()

        institution = Institution(
            name="Visual Resources Association", uri=URIRef("http://vraweb.org")
        )
        yield institution

        collection = Collection(
            institution_uri=institution.uri,
            title="Cataloging and Metadata Standards Committee Cataloging Examples",
            uri=URIRef(
                "http://vraweb.org/about/committees/vra-cataloging-and-metadata-standards-committee/"
            ),
        )
        yield collection

        yield from self.__transform_records(
            collection_uri=collection.uri,
            institution_uri=institution.uri,
            image_records=records_by_table["Images"],
            work_records=records_by_table["Works"],
        )

    def __parse_flattened(
        self, key_prefixes: Tuple[str, ...], fields: Dict[str, object]
    ):
        """
        Parse flattened keys such as Agent1Name.

        Handles three cases:
        1. Agent1 (<key prefix><value number>)
        2. Agent1Name (<key prefix><value number><sub key>)
        3. Agent1Name1 (<key prefix><value number><sub key><sub value number>)
        4. AgentName1 (<key prefix><sub key><value number>)

        Need to be given key prefixes in order to distinguish them from the sub key, for case 4.

        Returns a dict of
        {key_prefix: [{sub_key: [sub value, sub value]}]}
        """
        result = {}

        for key_prefix in key_prefixes:
            for key in list(sorted(fields.keys())):
                if not key.startswith(key_prefix):
                    continue
                value = fields.pop(key)
                key_suffix = key[len(key_prefix) :]
                assert key_suffix
                key_suffix_parts = []
                for key_suffix_part in re.split(r"(\d+)", key_suffix):
                    if not key_suffix_part:
                        continue
                    try:
                        key_suffix_part = int(key_suffix_part)
                    except ValueError:
                        pass
                    key_suffix_parts.append(key_suffix_part)

                if isinstance(key_suffix_parts[0], int):
                    # Agent1Name
                    value_number = key_suffix_parts.pop(0)
                else:
                    # AgentName1
                    assert isinstance(key_suffix_parts[-1], int)
                    value_number = key_suffix_parts.pop(-1)
                if key_suffix_parts:
                    assert isinstance(key_suffix_parts[0], str)
                    sub_key = key_suffix_parts.pop(0)
                    if key_suffix_parts:
                        # Agent1Name1
                        assert isinstance(key_suffix_parts[0], int)
                        sub_value_number = key_suffix_parts[0]
                    else:
                        # AgentName1
                        sub_value_number = None
                else:
                    # Agent1
                    sub_key = ""
                key_prefix_values = result.setdefault(key_prefix, [])
                while len(key_prefix_values) < value_number:
                    key_prefix_values.append({})
                sub_key_values = key_prefix_values[value_number - 1]
                if sub_value_number is None:
                    assert sub_key not in sub_key_values
                    sub_key_values[sub_key] = value
                else:
                    sub_key_values.setdefault(sub_key, []).append(value)
        return result

    def __transform_image_record(
        self,
        *,
        image_record: object,
        institution_uri: URIRef,
        work_uri: URIRef,
    ) -> Image:
        for image_thumbnail in image_record["fields"].get("IMAGE_Thumbnail", []):
            yield Image.create(
                depicts_uri=work_uri,
                institution_uri=institution_uri,
                uri=URIRef(image_thumbnail["thumbnails"]["full"]["url"]),
            )

    def __transform_records(
        self,
        *,
        collection_uri: URIRef,
        image_records: List[object],
        institution_uri: URIRef,
        work_records: List[object],
    ) -> Image:
        # Mutable dict of remaining (unyielded) image records
        images_records_by_id = {
            image_record["id"]: image_record for image_record in image_records
        }

        for work_record in work_records:
            yield from self.__transform_work_record(
                collection_uri=collection_uri,
                image_records_by_id=images_records_by_id,
                institution_uri=institution_uri,
                work_record=work_record,
            )

        for unused_image_record_id in images_records_by_id.keys():
            self._logger.warning("unused image record %s", unused_image_record_id)

    def __transform_work_record(
        self,
        *,
        collection_uri: URIRef,
        image_records_by_id: Dict[str, object],
        institution_uri: URIRef,
        work_record: object,
    ):
        work_uri = URIRef(
            self._record_url(
                table="Works",
                record_id=work_record["id"],
            )
        )

        work_record_fields = {}
        for key, value in work_record["fields"].items():
            if key == "Images":
                work_record_fields[key] = value
            elif key.startswith("WORK_"):
                work_record_fields[key[len("WORK_") :]] = value
        if not work_record_fields:
            return

        work_record_fields.pop("ID")

        work_title_display = work_record_fields.pop("TitleDisplay", None)
        work_title_pref = work_record_fields.pop("TitlePref", None)
        work_title = (
            work_title_display if work_title_display is not None else work_title_pref
        )
        assert work_title is not None
        work_abstract = work_record_fields.pop("DescriptionDisplay")
        try:
            work_rights = Rights(holder=work_record_fields.pop("DescriptionSource"))
        except KeyError:
            work_rights = None

        work_properties = []

        for (key, property_definition) in (
            ("AgentDisplay", PropertyDefinitions.CREATOR),
            ("CulturalContextDisplay", PropertyDefinitions.CULTURAL_CONTEXT),
            ("DateDisplay", PropertyDefinitions.DATE),
            ("LocationDisplay", PropertyDefinitions.SPATIAL),
            ("InscriptionDisplay", PropertyDefinitions.INSCRIPTION),
            ("MaterialDisplay", PropertyDefinitions.MATERIAL),
            ("MeasurementsDisplay", PropertyDefinitions.MEASUREMENTS),
            ("StylePeriodDisplay", PropertyDefinitions.STYLE_PERIOD),
            ("SubjectDisplay", PropertyDefinitions.SUBJECT),
            ("TechniqueDisplay", PropertyDefinitions.TECHNIQUE),
            ("TitleAlt", PropertyDefinitions.ALTERNATIVE_TITLE),
            ("WorktypeDisplay", PropertyDefinitions.WORK_TYPE),
        ):
            for value in work_record_fields.pop(key, "").split(":"):
                value = value.strip()
                if value:
                    work_properties.append(Property(property_definition, value))

        for ignore_key in (
            "LocationNotes",
            "TextrefName",
            "TextrefNameType",
            "TextrefRefid",
            "TextrefRefidType",
            "TitlePrefType",
        ):
            work_record_fields.pop(ignore_key, None)

        pprint(
            self.__parse_flattened(
                key_prefixes=(
                    "Agent",
                    "CulturalContext",
                    "Date",
                    "EarliestDate",
                    "LatestDate",
                    "Location",
                    "Material",
                    "Measurements",
                    "RelatedWork",
                    "RelationType",
                    "StylePeriod",
                    "Subject",
                    "Technique",
                    "Worktype",
                ),
                fields=work_record_fields,
            )
        )

        for image_record_id in work_record_fields.pop("Images", []):
            image_record = image_records_by_id.pop(image_record_id)
            yield from self.__transform_image_record(
                image_record=image_record,
                institution_uri=institution_uri,
                work_uri=work_uri,
            )

        yield Work(
            abstract=work_abstract,
            collection_uris=(collection_uri,),
            institution_uri=institution_uri,
            properties=tuple(work_properties),
            rights=work_rights,
            title=work_title,
            uri=work_uri,
        )

        for key, value in work_record_fields.items():
            self._logger.warning("unaccounted Work field %s = %s", key, value)
