import csv
from typing import Optional, Iterable

from paradicms_etl.loader import Loader
from paradicms_etl.model import Model
from paradicms_etl.models.work import Work
from rdflib import DCTERMS, Graph, Literal

from dressdiscover_etl.costume_core import CostumeCore
from dressdiscover_etl.namespaces import COCO
from dressdiscover_etl.transformers.costume_core_property_extractor import (
    CostumeCorePropertyExtractor,
)


class CostumeCorePropertyExtractorCsvFileLoader(Loader):
    def __init__(self, costume_core: Optional[CostumeCore] = None, **kwds):
        Loader.__init__(self, **kwds)
        self.__extractor = CostumeCorePropertyExtractor(costume_core=costume_core)

    def load(self, models: Iterable[Model]):
        with open(
            self._loaded_data_dir_path
            / (self._pipeline_id + "-extracted-costume-core-properties.csv"),
            "w+",
            newline="\n",
        ) as csv_file:
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=(
                    "object_uri",
                    "object_description",
                    "extracted_candidate",
                    "predicate",
                    "value",
                ),
            )
            csv_writer.writeheader()

            for model in models:
                if not isinstance(model, Work):
                    continue

                work = model
                work_resource = work.to_rdf(Graph())
                description = work_resource.value(DCTERMS.description)
                if not description or not isinstance(description, Literal):
                    self._logger.info(
                        "work %s has no literal description, skipping", work.uri
                    )
                    continue
                description = description.value.strip()
                if not description:
                    self._logger.info(
                        "work %s description is empty, skipping", work.uri
                    )
                    continue

                for candidate in self.__extractor.extract_candidates_from_text(
                    description
                ):
                    extracted_properties = (
                        self.__extractor.extract_properties_from_candidate(candidate)
                    )
                    if not extracted_properties:
                        csv_writer.writerow(
                            {
                                "object_description": description,
                                "object_uri": str(work.uri),
                                "extracted_candidate": candidate,
                            }
                        )
                        continue
                    for extracted_property in extracted_properties:
                        csv_writer.writerow(
                            {
                                "object_description": description,
                                "object_uri": str(work.uri),
                                "extracted_candidate": candidate,
                                "predicate": str(extracted_property.uri),
                                "value": extracted_property.value,
                            }
                        )
                for p, o in work_resource.predicate_objects():
                    if not str(p).startswith(str(COCO)):
                        continue
                    if not isinstance(o, Literal):
                        continue
                    csv_writer.writerow(
                        {
                            "object_description": description.encode(
                                "ascii", "replace"
                            ).decode("ascii"),
                            "object_uri": str(work.uri),
                            "predicate": str(p),
                            "value": o.value.encode("ascii", "replace").decode("ascii"),
                        }
                    )
