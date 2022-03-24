from paradicms_etl.loaders.rdf_file_loader import RdfFileLoader

from dressdiscover_etl.models.costume_core_predicate import CostumeCorePredicate
from dressdiscover_etl.models.costume_core_term import CostumeCoreTerm
from dressdiscover_etl.namespaces import COCO, bind_namespaces


class CostumeCoreOntologyRdfFileLoader(RdfFileLoader):
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

    def _new_graph(self):
        graph = RdfFileLoader._new_graph(self)
        bind_namespaces(graph)
        return graph
