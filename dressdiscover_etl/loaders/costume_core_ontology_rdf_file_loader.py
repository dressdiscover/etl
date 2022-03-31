from paradicms_etl.loaders.rdf_file_loader import RdfFileLoader
from rdflib import ConjunctiveGraph

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

    def _new_conjunctive_graph(self) -> ConjunctiveGraph:
        conjunctive_graph = RdfFileLoader._new_conjunctive_graph(self)
        bind_namespaces(conjunctive_graph.namespace_manager)
        return conjunctive_graph
