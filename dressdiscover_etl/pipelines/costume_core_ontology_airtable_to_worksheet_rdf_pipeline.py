from configargparse import ArgParser
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.extractors.costume_core_ontology_airtable_extractor import (
    CostumeCoreOntologyAirtableExtractor,
)
from dressdiscover_etl.loaders.dressdiscover_rdf_file_loader import (
    DressdiscoverRdfFileLoader,
)
from dressdiscover_etl.transformers.costume_core_ontology_airtable_to_worksheet_models_transformer import (
    CostumeCoreOntologyAirtableToWorksheetModelsTransformer,
)


class CostumeCoreOntologyAirtableToWorksheetRdfPipeline(Pipeline):
    ID = "costume_core_ontology"

    def __init__(self, *, api_key: str, **kwds):
        Pipeline.__init__(
            self,
            extractor=CostumeCoreOntologyAirtableExtractor(
                api_key=api_key, pipeline_id=self.ID, **kwds
            ),
            id=self.ID,
            loader=DressdiscoverRdfFileLoader(
                file_stem=self.ID + "_worksheet",
                format="ttl",
                pipeline_id=self.ID,
                **kwds,
            ),
            transformer=CostumeCoreOntologyAirtableToWorksheetModelsTransformer(
                pipeline_id=self.ID, **kwds
            ),
            **kwds,
        )

    @classmethod
    def add_arguments(cls, arg_parser: ArgParser):
        Pipeline.add_arguments(arg_parser)
        Pipeline._add_aws_credentials_arguments(arg_parser)
        arg_parser.add_argument("--api-key", required=True)


if __name__ == "__main__":
    CostumeCoreOntologyAirtableToWorksheetRdfPipeline.main()
