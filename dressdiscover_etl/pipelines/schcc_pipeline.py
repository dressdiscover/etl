from paradicms_etl.extractors.existing_file_extractor import ExistingFileExtractor
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.transformers.schcc_transformer import SchccTransformer


class SchccPipeline(Pipeline):
    ID = "schcc"

    def __init__(self, **kwds):
        Pipeline.__init__(
            self,
            extractor=ExistingFileExtractor(
                file_name="Smith CostumeCoreToolkit-MappingTemplate2 - Remediated.csv",
                pipeline_id=self.ID,
                **kwds
            ),
            id=self.ID,
            transformer=SchccTransformer(pipeline_id=self.ID, **kwds),
            **kwds
        )


if __name__ == "__main__":
    SchccPipeline.main()
