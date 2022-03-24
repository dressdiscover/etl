from paradicms_etl.extractors.existing_file_extractor import ExistingFileExtractor
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.transformers.penn_museum_transformer import PennMuseumTransformer


class PennMuseumPipeline(Pipeline):
    __ID = "penn_museum"

    def __init__(self, **kwds):
        Pipeline.__init__(
            self,
            extractor=ExistingFileExtractor(
                file_name="all.csv", pipeline_id=self.__ID, **kwds
            ),
            id=self.__ID,
            transformer=PennMuseumTransformer(pipeline_id=self.__ID, **kwds),
            **kwds
        )


if __name__ == "__main__":
    PennMuseumPipeline.main()
