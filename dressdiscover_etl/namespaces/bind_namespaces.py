from typing import TypeVar, Union

from rdflib import Graph
from rdflib.namespace import NamespaceManager

_NamespaceManagerT = TypeVar("_NamespaceManagerT", bound=Union[Graph, NamespaceManager])


def bind_namespaces(namespace_manager: _NamespaceManagerT) -> _NamespaceManagerT:
    from dressdiscover_etl.namespaces import COCO
    from paradicms_etl.namespaces import bind_namespaces as bind_paradicms_namespaces

    bind_paradicms_namespaces(namespace_manager)
    namespace_manager.bind("coco", COCO)
    return namespace_manager
