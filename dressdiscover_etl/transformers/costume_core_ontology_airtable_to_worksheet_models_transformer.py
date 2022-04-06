from typing import Dict, Tuple, Iterable, Union, List, Set, FrozenSet, Optional
from urllib.parse import quote

from paradicms_etl.model import Model
from paradicms_etl.models.creative_commons_licenses import CreativeCommonsLicenses
from paradicms_etl.models.image import Image
from paradicms_etl.models.image_dimensions import ImageDimensions
from paradicms_etl.models.license import License
from paradicms_etl.models.named_value import NamedValue
from paradicms_etl.models.rights import Rights
from paradicms_etl.models.rights_statements_dot_org_rights_statements import (
    RightsStatementsDotOrgRightsStatements,
)
from paradicms_etl.models.text import Text
from paradicms_etl.models.worksheet_feature import WorksheetFeature
from paradicms_etl.models.worksheet_feature_set import WorksheetFeatureSet
from paradicms_etl.transformer import Transformer
from rdflib import Graph, URIRef

from dressdiscover_etl.models.costume_core_term import CostumeCoreTerm
from dressdiscover_etl.namespaces import COCO


class CostumeCoreOntologyAirtableToWorksheetModelsTransformer(Transformer):
    def __init__(self, *args, **kwds):
        Transformer.__init__(self, *args, **kwds)
        self.__available_licenses_by_uri = {
            license.uri: license for license in CreativeCommonsLicenses.as_tuple()
        }
        odc_by_license = License.from_fields(
            identifier="ODC-By",
            title="Open Data Commons Attribution License (ODC-By) v1.0",
            uri=URIRef("http://opendatacommons.org/licenses/by/1-0/"),
            version="1.0",
        )
        self.__available_licenses_by_uri[odc_by_license.uri] = odc_by_license
        self.__available_license_uris = frozenset(
            self.__available_licenses_by_uri.keys()
        )

        self.__available_rights_statements_by_uri = {
            rights_statement.uri: rights_statement
            for rights_statement in RightsStatementsDotOrgRightsStatements.as_tuple()
        }
        self.__available_rights_statement_uris = frozenset(
            self.__available_rights_statements_by_uri.keys()
        )

    @staticmethod
    def __feature_set_uri(feature_set_record) -> URIRef:
        # Don't use "id" directly on the Costume Core namespace, since it's the same "id" as the work type term
        return COCO["featureSet/" + quote(feature_set_record["fields"]["feature_sets"])]

    def transform(self, *, records_by_table: Dict[str, Tuple]) -> Graph:  # type: ignore
        feature_records = tuple(
            record
            for record in records_by_table["features"]
            if "id" in record["fields"]
        )
        feature_set_records = tuple(
            record
            for record in records_by_table["feature_sets"]
            if "id" in record["fields"]
        )
        feature_value_records = tuple(
            record
            for record in records_by_table["feature_values"]
            if "id" in record["fields"]
        )
        image_records = tuple(
            record
            for record in records_by_table["images"]
            if "filename" in record["fields"]
        )
        # rights_licenses_records = tuple(
        #     record
        #     for record in records_by_table["rights_licenses"]
        #     if "Nickname" in record["fields"]
        # )

        # Track which licenses and rights statements we want to yield as we see references to them
        referenced_license_uris: Set[URIRef] = set()
        referenced_rights_statement_uris: Set[URIRef] = set()

        yield from self.__transform_feature_records(
            feature_records=feature_records,
            feature_set_records=feature_set_records,
            referenced_license_uris=referenced_license_uris,
            referenced_rights_statement_uris=referenced_rights_statement_uris,
        )

        yield from self.__transform_feature_set_records(
            feature_set_records=feature_set_records
        )

        yield from self.__transform_feature_value_records(
            feature_records=feature_records,
            feature_value_records=feature_value_records,
            image_records=image_records,
            referenced_license_uris=referenced_license_uris,
            referenced_rights_statement_uris=referenced_rights_statement_uris,
        )

        # Yield referenced licenses and rights statements once
        for license_uri in referenced_license_uris:
            yield self.__available_licenses_by_uri[license_uri]

        for rights_statement_uri in referenced_rights_statement_uris:
            yield self.__available_rights_statements_by_uri[rights_statement_uri]

    def __transform_feature_records(
        self,
        feature_records,
        feature_set_records,
        referenced_license_uris: Set[URIRef],
        referenced_rights_statement_uris: Set[URIRef],
    ) -> Iterable[Model]:
        for feature_record in feature_records:
            feature_record_fields = feature_record["fields"]

            if "display_name_en" not in feature_record_fields:
                continue
            if "URI" not in feature_record_fields:
                continue

            feature_set_uris = set()
            for feature_set_record in feature_set_records:
                for feature_record_id in feature_set_record["fields"].get(
                    "features", []
                ):
                    if feature_record_id == feature_record["id"]:
                        feature_set_uris.add(self.__feature_set_uri(feature_set_record))

            if not feature_set_uris:
                self._logger.warning(
                    "feature %s does not belong to any feature sets",
                    feature_record["fields"]["id"],
                )
                continue

            yield WorksheetFeature.from_fields(
                abstract=self.__transform_description(
                    record_fields=feature_record_fields,
                    referenced_license_uris=referenced_license_uris,
                    referenced_rights_statement_uris=referenced_rights_statement_uris,
                ),
                feature_set_uris=tuple(feature_set_uris),
                title=feature_record_fields["display_name_en"],
                uri=URIRef(feature_record_fields["URI"]),
            )

    def __transform_feature_set_records(
        self,
        *,
        feature_set_records,
    ) -> Iterable[Model]:
        for feature_set_record in feature_set_records:
            yield WorksheetFeatureSet.from_fields(
                title=feature_set_record["fields"]["display_name_en"],
                uri=self.__feature_set_uri(feature_set_record),
            )

    def __transform_feature_value_records(
        self,
        *,
        feature_records,
        feature_value_records,
        image_records,
        referenced_license_uris: Set[URIRef],
        referenced_rights_statement_uris: Set[URIRef],
    ) -> Iterable[Model]:
        image_records_by_id = {
            image_record["id"]: image_record for image_record in image_records
        }

        for feature_value_record in feature_value_records:
            feature_value_record_fields = feature_value_record["fields"]

            if not feature_value_record_fields["id"].startswith("CC"):
                continue

            if "display_name_en" not in feature_value_record_fields:
                continue

            feature_uris = []
            for feature_record_id in feature_value_record_fields.get("features", []):
                for feature_record in feature_records:
                    if feature_record["id"] == feature_record_id:
                        feature_uris.append(URIRef(feature_record["fields"]["URI"]))
                        break

            if not feature_uris:
                self._logger.warning(
                    "feature value %s does not belong to any features",
                    feature_value_record_fields["id"],
                )
                continue

            # aat_id=fields.get("AATID"),
            #     wikidata_id=fields.get("WikidataID"),

            feature_value_uri = COCO[feature_value_record_fields["id"]]
            feature_value = NamedValue.from_fields(
                abstract=self.__transform_description(
                    record_fields=feature_value_record_fields,
                    referenced_license_uris=referenced_license_uris,
                    referenced_rights_statement_uris=referenced_rights_statement_uris,
                ),
                property_uris=tuple(feature_uris),
                title=feature_value_record_fields["display_name_en"],
                value=feature_value_uri,
                uri=feature_value_uri,
            )
            yield feature_value

            image_record_id = feature_value_record_fields.get("image_filename")
            if image_record_id:
                image_record_id = image_record_id[0]
                assert image_record_id

                image_record = image_records_by_id[image_record_id]
                image_filename = image_record["fields"]["filename"]
                image_rights = self.__transform_rights(
                    key_prefix="image",
                    record_fields=feature_value_record_fields,
                    referenced_license_uris=referenced_license_uris,
                    referenced_rights_statement_uris=referenced_rights_statement_uris,
                )

                full_size_image = Image.from_fields(
                    depicts_uri=feature_value.uri,
                    rights=image_rights,
                    uri=URIRef(
                        CostumeCoreTerm.FULL_SIZE_IMAGE_BASE_URL + image_filename
                    ),
                )
                yield full_size_image

                yield Image.from_fields(
                    depicts_uri=feature_value.uri,
                    exact_dimensions=ImageDimensions(height=200, width=200),
                    original_image_uri=full_size_image.uri,
                    rights=image_rights,
                    uri=URIRef(CostumeCoreTerm.THUMBNAIL_BASE_URL + image_filename),
                )

    def __transform_description(
        self,
        *,
        record_fields: Dict[str, Union[str, List[str], None]],
        referenced_license_uris: Set[URIRef],
        referenced_rights_statement_uris: Set[URIRef],
    ) -> Optional[Text]:
        description_text_en = record_fields.get("description_text_en")
        if not description_text_en:
            return None
        return Text.from_fields(
            rights=self.__transform_rights(
                key_prefix="description",
                record_fields=record_fields,
                referenced_license_uris=referenced_license_uris,
                referenced_rights_statement_uris=referenced_rights_statement_uris,
            ),
            value=description_text_en,
        )

    def __transform_rights(
        self,
        *,
        key_prefix: str,
        record_fields: Dict[str, Union[str, List[str], None]],
        referenced_license_uris: Set[URIRef],
        referenced_rights_statement_uris: Set[URIRef],
    ) -> Rights:
        """
        Utility function to transform a prefixed subset of fields into a Rights model.
        """

        def get_first_list_element(list_: Union[str, List[str], None]):
            if list_ is None:
                return None
            if not isinstance(list_, list):
                return list_
            assert len(list_) == 1
            return list_[0]

        def transform_rights_uri(
            available_rights_uris: FrozenSet[URIRef],
            rights_uri_str: Union[None, str],
            referenced_rights_uris: Set[URIRef],
        ) -> Union[None, str, URIRef]:
            if not rights_uri_str:
                return None

            rights_uri = URIRef(rights_uri_str)
            if rights_uri in available_rights_uris:
                referenced_rights_uris.add(rights_uri)
                return rights_uri

            if str(rights_uri).startswith("https://"):
                http_rights_uri = URIRef("http://" + rights_uri[len("https://") :])
                if http_rights_uri in available_rights_uris:
                    referenced_rights_uris.add(http_rights_uri)
                    return http_rights_uri

            if id(available_rights_uris) != id(
                self.__available_rights_statement_uris
            ) or rights_uri not in (
                URIRef("https://creativecommons.org/publicdomain/zero/1.0/"),
                URIRef("https://creativecommons.org/publicdomain/mark/1.0/"),
            ):
                self._logger.warning("unknown rights URI: %s", rights_uri)

        return Rights.from_fields(
            creator=get_first_list_element(
                record_fields.get(f"{key_prefix}_rights_author")
            ),
            license=transform_rights_uri(
                available_rights_uris=self.__available_license_uris,
                rights_uri_str=get_first_list_element(
                    record_fields.get(f"{key_prefix}_rights_license")
                ),
                referenced_rights_uris=referenced_license_uris,
            ),
            statement=transform_rights_uri(
                available_rights_uris=self.__available_rights_statement_uris,
                rights_uri_str=get_first_list_element(
                    record_fields.get(f"{key_prefix}_rights_statement")
                ),
                referenced_rights_uris=referenced_rights_statement_uris,
            ),
            # source_name=get_first_list_element(
            #     fields[f"{key_prefix}_rights_source_name"]
            # ),
            # source_url=get_first_list_element(
            #     fields[f"{key_prefix}_rights_source_url"]
            # ),
        )
