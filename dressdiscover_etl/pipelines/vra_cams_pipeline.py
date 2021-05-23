from typing import Optional

from paradicms_etl._loader import _Loader
from paradicms_etl._pipeline import _Pipeline
from paradicms_etl.extractors.airtable_extractor import AirtableExtractor
from paradicms_etl.image_archivers.s3_image_archiver import S3ImageArchiver
from paradicms_etl.loaders.gui.gui_loader import GuiLoader
from paradicms_etl.loaders.gui.s3_gui_deployer import S3GuiDeployer

from dressdiscover_etl.transformers.vra_cams_transformer import VraCamsTransformer


class VraCamsPipeline(_Pipeline):
    __BASE_ID = "appNiGlLwG3G3DBkl"
    __ID = "vra_cams"

    def __init__(self, api_key: str, loader: Optional[_Loader] = None, **kwds):
        if loader is None:
            loader = GuiLoader(
                gui="bootstrap-collection",
                deployer=S3GuiDeployer(
                    s3_bucket_name="vra-cams.dressdiscover.org",
                    **kwds,
                ),
                image_archiver=S3ImageArchiver(
                    s3_bucket_name="dressdiscover-images", **kwds
                ),
                pipeline_id=self.__ID,
                **kwds,
            )

        _Pipeline.__init__(
            self,
            extractor=AirtableExtractor(
                api_key=api_key,
                base_id=self.__BASE_ID,
                pipeline_id=self.__ID,
                tables=(
                    "Images",
                    "Works",
                ),
                **kwds,
            ),
            id=self.__ID,
            loader=loader,
            transformer=VraCamsTransformer(
                base_id=self.__BASE_ID,
                pipeline_id=self.__ID,
                **kwds,
            ),
            **kwds,
        )

    @classmethod
    def add_arguments(cls, arg_parser):
        _Pipeline.add_arguments(arg_parser)
        _Pipeline._add_aws_credentials_arguments(arg_parser)
        arg_parser.add_argument("--api-key", required=True)


if __name__ == "__main__":
    VraCamsPipeline.main()
