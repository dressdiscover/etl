import csv
from pathlib import Path
from typing import Dict, Generator, Tuple

from paradicms_etl._model import _Model
from paradicms_etl._transformer import _Transformer
from paradicms_etl.models.collection import Collection
from paradicms_etl.models.creative_commons_licenses import CreativeCommonsLicenses
from paradicms_etl.models.dublin_core_property_definitions import (
    DublinCorePropertyDefinitions,
)
from paradicms_etl.models.institution import Institution
from paradicms_etl.models.object import Object
from paradicms_etl.models.property import Property
from paradicms_etl.models.rights import Rights
from paradicms_etl.models.vra_core_property_definitions import (
    VraCorePropertyDefinitions,
)
from rdflib import URIRef


class PennMuseumTransformer(_Transformer):
    __RELEVANT_OBJECT_NAMES = {"Dress", "Clothing", "Hat", "Shirt", "Skirt"}
    __IGNORE_KEYS = (
        "emuIRN",
        "iconography",
        "measurement_height",
        "measurement_length",
        "measurement_outside_diameter",
        "measurement_tickness",
        "measurement_unit",
        "measurement_width",
        "native_name",
        "other_numbers",
    )

    def transform(self, *, file_path: Path):
        yield CreativeCommonsLicenses.BY
        yield from DublinCorePropertyDefinitions.as_tuple()
        yield from VraCorePropertyDefinitions.as_tuple()

        institution = Institution(
            name="Penn Museum",
            rights=Rights(
                license=URIRef("http://creativecommons.org/licenses/by/3.0/"),
                statement="Copyright Penn Museum",
            ),
            uri=URIRef("http://penn.museum"),
        )
        yield institution

        collections_by_curatorial_section = {}

        with open(file_path, encoding="utf-8") as csv_file:
            for csv_row in csv.DictReader(csv_file):
                csv_row = csv_row.copy()

                curatorial_section = csv_row.pop("curatorial_section")

                collection = collections_by_curatorial_section.get(curatorial_section)
                if collection is None:
                    collection = Collection(
                        institution_uri=institution.uri,
                        title=curatorial_section,
                        uri=URIRef(
                            f"http://www.penn.museum/about-collections/curatorial-sections/{'-'.join(part.lower() for part in curatorial_section.split(' '))}-section"
                        ),
                    )
                    new_collection = True
                else:
                    new_collection = False

                for model in self.__transform_csv_row(
                    collection=collection, csv_row=csv_row, institution=institution
                ):
                    if isinstance(model, Object):
                        if new_collection:
                            # Ensure the collection is referenced before yielding it
                            collections_by_curatorial_section[
                                curatorial_section
                            ] = collection
                            yield collection

                    yield model

    def __transform_csv_row(
        self,
        *,
        collection: Collection,
        csv_row: Dict[str, str],
        institution: Institution,
    ) -> Generator[_Model, None, None]:
        csv_row = {
            key.strip().encode("ascii", "ignore").decode("ascii"): value.strip()
            for key, value in csv_row.items()
            if key.strip() and value.strip()
        }

        def pop_multiple_values(key: str) -> Tuple[str, ...]:
            values_joined = csv_row.pop(key, None)
            if values_joined is None:
                return ()
            return values_joined.split("|")

        description = csv_row.pop("description", None)
        if not description:
            return

        relevant_object_name = None
        for object_name in pop_multiple_values("object_name"):
            if object_name in self.__RELEVANT_OBJECT_NAMES:
                relevant_object_name = object_name
                break
        if relevant_object_name is None:
            return

        properties = set()
        if description:
            properties.add(
                Property(DublinCorePropertyDefinitions.DESCRIPTION, description)
            )
        properties.add(Property(DublinCorePropertyDefinitions.TITLE, object_name))

        for key, property_definition in (
            ("accession_credit_line", DublinCorePropertyDefinitions.CONTRIBUTOR),
            ("creator", DublinCorePropertyDefinitions.CREATOR),
            ("culture", DublinCorePropertyDefinitions.CULTURAL_CONTEXT),
            ("culture_area", DublinCorePropertyDefinitions.SPATIAL),
            ("date_made", DublinCorePropertyDefinitions.DATE_CREATED),
            ("date_made_early", VraCorePropertyDefinitions.EARLIEST_DATE),
            ("date_made_late", VraCorePropertyDefinitions.LATEST_DATE),
            ("material", VraCorePropertyDefinitions.MATERIAL),
            ("object_number", DublinCorePropertyDefinitions.IDENTIFIER),
            ("period", DublinCorePropertyDefinitions.TEMPORAL),
            ("provenience", DublinCorePropertyDefinitions.PROVENANCE),
            ("technique", VraCorePropertyDefinitions.TECHNIQUE),
        ):
            for value in pop_multiple_values(key):
                properties.add(Property(property_definition, value))

        yield Object(
            abstract=description,
            collection_uris=(collection.uri,),
            institution_uri=institution.uri,
            properties=tuple(properties),
            title=relevant_object_name,
            uri=URIRef(csv_row.pop("url")),
        )

        for ignore_key in self.__IGNORE_KEYS:
            csv_row.pop(ignore_key, None)

        for key, value in csv_row.items():
            self._logger.warning("unparsed %s = %s", key, value)
