from configargparse import ArgParser
from paradicms_etl.extractors.airtable_extractor import AirtableExtractor
from paradicms_etl.loaders.composite_loader import CompositeLoader
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.loaders.costume_core_ontology_py_loader import (
    CostumeCoreOntologyPyLoader,
)
from dressdiscover_etl.loaders.costume_core_ontology_rdf_file_loader import (
    CostumeCoreOntologyRdfFileLoader,
)
from dressdiscover_etl.transformers.costume_core_ontology_airtable_to_costume_core_models_transformer import (
    CostumeCoreOntologyAirtableToCostumeCoreModelsTransformer,
)


class CostumeCoreOntologyAirtableToRdfPipeline(Pipeline):
    ID = "costume_core_ontology"

    def __init__(self, *, api_key: str, ontology_version: str, **kwds):
        Pipeline.__init__(
            self,
            extractor=AirtableExtractor(
                api_key=api_key,
                base_id="appfEYYWWn3CqSAxW",
                pipeline_id=self.ID,
                tables=(
                    "feature_values",
                    "features",
                    "feature_sets",
                    "images",
                    "rights_licenses",
                ),
                **kwds,
            ),
            id=self.ID,
            loader=CompositeLoader(
                pipeline_id=self.ID,
                loaders=(
                    CostumeCoreOntologyPyLoader(pipeline_id=self.ID, **kwds),
                    CostumeCoreOntologyRdfFileLoader(
                        format="ttl", pipeline_id=self.ID, **kwds
                    ),
                    CostumeCoreOntologyRdfFileLoader(
                        format="xml", pipeline_id=self.ID, **kwds
                    ),
                ),
            ),
            transformer=CostumeCoreOntologyAirtableToCostumeCoreModelsTransformer(
                ontology_version=ontology_version, pipeline_id=self.ID, **kwds
            ),
            **kwds,
        )

    @classmethod
    def add_arguments(cls, arg_parser: ArgParser):
        Pipeline.add_arguments(arg_parser)
        Pipeline._add_aws_credentials_arguments(arg_parser)
        arg_parser.add_argument("--api-key", required=True)
        arg_parser.add_argument("--ontology-version", required=True)


if __name__ == "__main__":
    CostumeCoreOntologyAirtableToRdfPipeline.main()
