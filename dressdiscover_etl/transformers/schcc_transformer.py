import csv
from pathlib import Path
from typing import Dict, Generator, Optional, List, Union

from paradicms_etl.model import Model
from paradicms_etl.models.collection import Collection
from paradicms_etl.models.institution import Institution
from paradicms_etl.models.property import Property
from paradicms_etl.models.rights import Rights
from paradicms_etl.models.work import Work
from paradicms_etl.namespaces import VRA
from paradicms_etl.transformer import Transformer
from rdflib import URIRef, DCTERMS
from rdflib.term import Node

from dressdiscover_etl.costume_core import CostumeCore
from dressdiscover_etl.models import costume_core_predicates
from dressdiscover_etl.models.costume_core_predicate import CostumeCorePredicate


class SchccTransformer(Transformer):
    def __init__(self, **kwds):
        Transformer.__init__(self, **kwds)
        self.__costume_core = CostumeCore()

    def transform(self, *, file_path: Path):  # type: ignore
        collection = None
        institution = None

        with open(file_path, "r", encoding="utf-8") as csv_file:
            for csv_row in csv.DictReader(csv_file):
                csv_row = {
                    key.strip(): value.strip()
                    for key, value in csv_row.items()
                    if key.strip() and value.strip()
                }
                if not csv_row:
                    continue

                if institution is None:
                    assert collection is None

                    institution = Institution(
                        name="Smith College",
                        uri=URIRef("http://www.smith.edu/"),
                    )
                    yield institution

                    collection = Collection(
                        institution_uri=institution.uri,
                        title=csv_row["Holding Institution"],
                        uri=URIRef("http://schistoricclothing.com/"),
                    )
                    yield collection
                else:
                    assert collection is not None

                yield from self.__transform_csv_row(
                    collection=collection, csv_row=csv_row, institution=institution
                )

    def __transform_csv_row(
        self,
        *,
        collection: Collection,
        csv_row: Dict[str, str],
        institution: Institution,
    ) -> Generator[Work, None, None]:
        int(csv_row["SSID"])
        object_uri = URIRef("urn:sharedshelf:schcc:" + csv_row["SSID"])

        properties: List[Property] = []
        properties_by_uri: Dict[str, List[Property]] = {}

        def transform_csv_column(
            *,
            csv_column_key: str,
            multi: bool,
            costume_core_predicate: Optional[CostumeCorePredicate] = None,
            property_uri: Optional[URIRef] = None,
        ):
            value = csv_row.pop(csv_column_key, None)
            if not value:
                return
            if multi:
                values = []
                for value in value.split("|"):
                    value = value.strip()
                    if not value:
                        continue
                    values.append(value)
            else:
                assert "|" not in value
                values = [value]

            if not values:
                return

            if costume_core_predicate is not None:
                property_uri = URIRef(costume_core_predicate.uri)
            elif property_uri is None:
                raise ValueError("must specify Costume Core predicate or property URI")

            for value in values:
                property_ = Property(property_uri, value)
                properties.append(property_)
                properties_by_uri.setdefault(property_uri, []).append(property_)
                # if costume_core_terms is not None:
                #     for costume_core_term in costume_core_terms:
                #         if costume_core_term.display_name_en == value:
                #             self.resource.add(property, URIRef(costume_core_term.uri))
                #             break

        transform_csv_column(
            multi=False,
            csv_column_key="Alternative Title",
            property_uri=DCTERMS.alternative,
        )
        csv_row.pop("Cataloguer With Date", None)  # Ignore
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.classification,
            csv_column_key="Classification",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.collar,
            csv_column_key="Collar",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.colorMain,
            csv_column_key="Color Main",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.colorSecondary,
            csv_column_key="Color Secondary",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.condition,
            csv_column_key="Condition Term",
        )
        transform_csv_column(
            multi=False,
            csv_column_key="Creator",
            property_uri=DCTERMS.creator,
        )
        transform_csv_column(
            multi=True,
            costume_core_predicate=costume_core_predicates.culturalContext,
            csv_column_key="Culture",
        )
        transform_csv_column(
            multi=False,
            csv_column_key="Date",
            property_uri=DCTERMS.date,
        )
        for (date_csv_column_key, date_property_uri) in (
            ("Date Earliest", VRA.earliestDate),
            ("Date Latest", VRA.latestDate),
        ):
            date_value = csv_row.pop(date_csv_column_key, None)
            if not date_value:
                continue
            # date_value = int(date_value)
            # self.resource.add(date_property, Literal(date_value, datatype=XSD.int))
        transform_csv_column(
            multi=False,
            csv_column_key="Description",
            property_uri=DCTERMS.description,
        )
        csv_row.pop("Description Autofill", None)  # Created from other columns
        transform_csv_column(
            multi=True,
            costume_core_predicate=costume_core_predicates.dressType,
            csv_column_key="Dress Type",
        )
        # Skip Donor
        transform_csv_column(
            multi=True,
            costume_core_predicate=costume_core_predicates.function,
            csv_column_key="Function",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.gender,
            csv_column_key="Gender",
        )
        # transform_csv_column(
        #     multi=False,
        #     csv_column_key="Grain",
        #     property_uri=URIRef(costume_core_predicates.grain.uri),
        # )
        transform_csv_column(
            multi=False,
            csv_column_key="Identifier",
            property_uri=DCTERMS.identifier,
        )
        # Skip Label
        transform_csv_column(
            multi=True,
            costume_core_predicate=costume_core_predicates.lifeStages,
            csv_column_key="Life Stages",
        )
        csv_row.pop("Measurements Display", None)  # Ignore for now, no predicates
        csv_row.pop("Measurements Autofill", None)  # Created from other columns
        transform_csv_column(
            multi=True,
            csv_column_key="Medium",
            property_uri=DCTERMS.medium,
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.neckline,
            csv_column_key="Neckline",
        )
        transform_csv_column(
            multi=True,
            costume_core_predicate=costume_core_predicates.hasTechnique,
            csv_column_key="Technique",
        )
        transform_csv_column(
            multi=True,
            csv_column_key="Region",
            property_uri=DCTERMS.spatial,
        )
        # Shared Shelf fields
        csv_row.pop("SSID")
        csv_row.pop("Source ID[66858]", None)
        csv_row.pop("SC Accession[66859]", None)
        csv_row.pop("SC Batch Number[66863]", None)
        csv_row.pop("SC Order[66860]", None)
        csv_row.pop("SC Work Number[66862]", None)
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.skirtType,
            csv_column_key="Skirt Type",
        )
        # transform_csv_column(
        #     multi=False,
        #     costume_core_predicate=costume_core_predicates.skirtLength,
        #     csv_column_key="Skirt Length",
        # )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.sleeveType,
            csv_column_key="Sleeve Type",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.sleeveLength,
            csv_column_key="Sleeve Length",
        )
        transform_csv_column(
            multi=True,
            csv_column_key="Style Period",
            property_uri=DCTERMS.temporal,
        )
        transform_csv_column(
            multi=False,
            csv_column_key="Subject",
            property_uri=DCTERMS.subject,
        )
        transform_csv_column(
            multi=False,
            csv_column_key="Title",
            property_uri=DCTERMS.title,
        )
        type_ = csv_row.pop("Type")
        assert type_ == "Physical object", type_
        # self.resource.add(DCTERMS.type, DCMITYPE.PhysicalObject)
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.waistline,
            csv_column_key="Waistline",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.workType,
            csv_column_key="Work Type",
        )
        transform_csv_column(
            multi=False,
            costume_core_predicate=costume_core_predicates.wornBy,
            csv_column_key="Worn by",
        )

        holding_institution = csv_row.pop("Holding Institution", None)
        rights = Rights.from_fields(
            holder=holding_institution if holding_institution is not None else None,
            # statement=RightsValue(
            #     text=csv_row.pop("Rights Holder"),
            #     uri=URIRef(csv_row.pop("Rights")),
            # ),
            statement=csv_row.pop("Rights Holder"),
        )

        for key, value in csv_row.items():
            self._logger.warn("object %s: unaccounted %s = %s", object_uri, key, value)

        def get_first_property_value(property_uri: URIRef) -> Union[Model, Node, None]:
            property_uri_properties = properties_by_uri.get(property_uri)
            if property_uri_properties is None:
                return None
            return property_uri_properties[0].value

        object_title = get_first_property_value(DCTERMS.title)
        if object_title is None:
            self._logger.warn("object %s has no title, ignoring", object_uri)
            return

        yield Work(
            abstract=get_first_property_value(DCTERMS.description),
            collection_uris=(collection.uri,),
            institution_uri=institution.uri,
            properties=tuple(properties),
            rights=rights,
            title=object_title,
            uri=object_uri,
        )
