from paradicms_etl.loaders.rdf_file_loader import RdfFileLoader
from rdflib import ConjunctiveGraph

from dressdiscover_etl.namespaces import bind_namespaces


class DressdiscoverRdfFileLoader(RdfFileLoader):
    def _new_conjunctive_graph(self) -> ConjunctiveGraph:
        conjunctive_graph = RdfFileLoader._new_conjunctive_graph(self)
        bind_namespaces(conjunctive_graph.namespace_manager)
        return conjunctive_graph
