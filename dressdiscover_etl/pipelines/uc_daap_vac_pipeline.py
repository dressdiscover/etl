from paradicms_etl.extractors.luna_extractor import LunaExtractor
from paradicms_etl.pipeline import Pipeline

from dressdiscover_etl.transformers.uc_daap_vac_transformer import UcDaapVacTransformer


class UcDaapVacPipeline(Pipeline):
    """
    Pipeline for the Visual Arts Collection at the Library for Design, Architecture, Art, and Planning at the University of Cincinnati
    """

    ID = "uc_daap_vac"

    def __init__(self, **kwds):
        Pipeline.__init__(
            self,
            extractor=LunaExtractor(
                base_url="https://digital.libraries.uc.edu/",
                pipeline_id=self.ID,
                query={
                    "bs": "200",
                    "lc": "univcincin~38~38",
                    "q": '="Cashin, Bonnie, 1915-2000"',
                },
                **kwds
            ),
            transformer=UcDaapVacTransformer(pipeline_id=self.ID, **kwds),
            id=self.ID,
            **kwds
        )


if __name__ == "__main__":
    UcDaapVacPipeline.main()
