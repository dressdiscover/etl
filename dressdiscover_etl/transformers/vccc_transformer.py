from typing import Optional

from paradicms_etl.models.collection import Collection

from dressdiscover_etl.transformers.costume_core_omeka_classic_transformer import (
    CostumeCoreOmekaClassicTransformer,
)


class VcccTransformer(CostumeCoreOmekaClassicTransformer):
    def __init__(self, **kwds):
        CostumeCoreOmekaClassicTransformer.__init__(
            self,
            fullsize_max_height_px=600,
            fullsize_max_width_px=600,
            institution_name="Vassar College Costume Collection",
            institution_rights="Copyright Vassar College. All rights reserved.",
            institution_uri="https://vcomeka.com/vccc/",
            square_thumbnail_height_px=150,
            square_thumbnail_width_px=150,
            thumbnail_max_height_px=200,
            thumbnail_max_width_px=200,
            **kwds
        )

    def _transform_collection(
        self, *, omeka_collection, **kwds
    ) -> Optional[Collection]:
        if omeka_collection["url"] != "https://vcomeka.com/vccc/api/collections/1":
            return None  # Ignore all but  the "Costumes and Textiles" collection
        return CostumeCoreOmekaClassicTransformer._transform_collection(
            self, omeka_collection=omeka_collection, **kwds
        )

    def _transform_file(self, **kwds):
        return tuple(
            image.replace(copyable=False)
            for image in CostumeCoreOmekaClassicTransformer._transform_file(
                self, **kwds
            )
        )
