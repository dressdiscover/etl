from typing import Optional

from paradicms_etl.loader import Loader
from paradicms_etl.loaders.composite_loader import CompositeLoader
from paradicms_etl.loaders.rdf_file_loader import RdfFileLoader
from paradicms_etl.pipeline import Pipeline
from paradicms_gui.deployers.s3_deployer import S3Deployer  # type: ignore
from paradicms_gui.image_archivers.s3_image_archiver import S3ImageArchiver  # type: ignore
from paradicms_gui.loaders.gui_loader import GuiLoader  # type: ignore

from dressdiscover_etl.extractors.costume_core_data_airtable_extractor import (
    CostumeCoreDataAirtableExtractor,
)
from dressdiscover_etl.loaders.costume_core_property_extractor_csv_file_loader import (
    CostumeCorePropertyExtractorCsvFileLoader,
)
from dressdiscover_etl.transformers.costume_core_airtable_transformer import (
    CostumeCoreAirtableTransformer,
)


class CostumeCoreTemplatePipeline(Pipeline):
    __BASE_ID = "appgU92SdGTwPIVNg"
    __ID = "costume_core_template"

    def __init__(self, api_key: str, loader: Optional[Loader] = None, **kwds):
        if loader is None:
            loader = CompositeLoader(
                loaders=(
                    CostumeCorePropertyExtractorCsvFileLoader(
                        pipeline_id=self.__ID, **kwds
                    ),
                    RdfFileLoader(pipeline_id=self.__ID, **kwds),
                    GuiLoader(
                        app="collection",
                        deployer=S3Deployer(
                            s3_bucket_name="costumecoretemplate.dressdiscover.org",
                            **kwds,
                        ),
                        image_archiver=S3ImageArchiver(
                            s3_bucket_name="dressdiscover-images", **kwds
                        ),
                        pipeline_id=self.__ID,
                        **kwds,
                    ),
                ),
                pipeline_id=self.__ID,
                **kwds,
            )

        Pipeline.__init__(
            self,
            extractor=CostumeCoreDataAirtableExtractor(
                api_key=api_key, base_id=self.__BASE_ID, pipeline_id=self.__ID, **kwds
            ),
            id=self.__ID,
            loader=loader,
            transformer=CostumeCoreAirtableTransformer(
                base_id=self.__BASE_ID,
                collection_title="Costume Core Template Airtable",
                collection_uri="https://airtable.com/" + self.__BASE_ID,
                institution_name="Costume Core Template",
                institution_uri="http://www.ardenkirkland.com/costumecore/",
                institution_rights="Copyright Arden Kirkland. All rights reserved.",
                pipeline_id=self.__ID,
                **kwds,
            ),
            **kwds,
        )

    @classmethod
    def add_arguments(cls, arg_parser):
        Pipeline.add_arguments(arg_parser)
        Pipeline._add_aws_credentials_arguments(arg_parser)
        arg_parser.add_argument("--api-key", required=True)


if __name__ == "__main__":
    CostumeCoreTemplatePipeline.main()
