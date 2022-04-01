from paradicms_etl.extractors.nop_extractor import NopExtractor
from paradicms_etl.loaders.nop_loader import NopLoader
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.transformers.costume_core_models_to_paradicms_models_transformer import (
    CostumeCoreModelsToParadicmsModelsTransformer,
)


class CostumeCoreModelsToParadicmsGuiPipeline(Pipeline):
    ID = "costume_core_models_to_paradicms_gui"

    def __init__(self, **kwds):
        Pipeline.__init__(
            self,
            extractor=NopExtractor(pipeline_id=self.ID),
            id=self.ID,
            loader=NopLoader(pipeline_id=self.ID),
            transformer=CostumeCoreModelsToParadicmsModelsTransformer(
                pipeline_id=self.ID, **kwds
            ),
            **kwds,
        )


if __name__ == "__main__":
    CostumeCoreModelsToParadicmsGuiPipeline.main()
