from configargparse import ArgParser
from paradicms_etl.extractors.existing_file_extractor import ExistingFileExtractor
from paradicms_etl.pipeline import Pipeline
from paradicms_gui.deployers.s3_deployer import S3Deployer  # type: ignore
from paradicms_gui.image_archivers.s3_image_archiver import S3ImageArchiver  # type: ignore
from paradicms_gui.loaders.gui_loader import GuiLoader  # type: ignore

from dressdiscover_etl.transformers.iastate_amd_354_transformer import (
    IastateAmd354Transformer,
)


class IastateAmd354Pipeline(Pipeline):
    ID = "iastate_amd_354"

    def __init__(self, **kwds):
        Pipeline.__init__(
            self,
            id=self.ID,
            extractor=ExistingFileExtractor(
                file_name="AMD 354 Image database.csv",
                pipeline_id=self.ID,
                **kwds,
            ),
            loader=GuiLoader(
                app="collection",
                deployer=S3Deployer(
                    s3_bucket_name="iastate-amd354.dressdiscover.org", **kwds
                ),
                image_archiver=S3ImageArchiver(
                    s3_bucket_name="dressdiscover-images", **kwds
                ),
                pipeline_id=self.ID,
                **kwds,
            ),
            transformer=IastateAmd354Transformer(pipeline_id=self.ID, **kwds),
            **kwds,
        )

    @classmethod
    def add_arguments(cls, arg_parser: ArgParser) -> None:
        Pipeline.add_arguments(arg_parser)
        Pipeline._add_aws_credentials_arguments(arg_parser)


if __name__ == "__main__":
    IastateAmd354Pipeline.main()
