from paradicms_etl.loaders.rdf_file_loader import RdfFileLoader

from dressdiscover_etl.loaders.dressdiscover_rdf_file_loader import (
    DressdiscoverRdfFileLoader,
)
from dressdiscover_etl.models.costume_core_predicate import CostumeCorePredicate
from dressdiscover_etl.models.costume_core_term import CostumeCoreTerm
from dressdiscover_etl.namespaces import COCO


class CostumeCoreOntologyRdfFileLoader(DressdiscoverRdfFileLoader):
    def _flush(self, models):
        RdfFileLoader._flush(
            self,
            tuple(
                model
                for model in models
                if isinstance(model, (CostumeCorePredicate, CostumeCoreTerm))
                and str(model.uri).startswith(str(COCO))
            ),
        )
