from typing import NamedTuple, Optional


class CostumeCoreRights(NamedTuple):
    author: str
    license_uri: Optional[str]
    rights_statement_uri: Optional[str]
    source_name: str
    source_url: str
