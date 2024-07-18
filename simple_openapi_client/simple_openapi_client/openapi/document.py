from dataclasses import dataclass
from typing import Dict, Optional, List

from simple_openapi_client.openapi.info import Info
from simple_openapi_client.openapi.info import Tags
from simple_openapi_client.openapi.path import Path


@dataclass
class Document:

    openapi: str  # OpenAPI version

    info: Info
    paths: Dict[str, Path]
    tags: Optional[Tags] = List[Dict[str, str]]

    def __post_init__(self):
        self.info = Info(**self.info)
        self.paths = {k: Path(**v) for k, v in self.paths.items()}
        self.tags = Tags(**self.tags)

    def __repr__(self) -> str:
        return f'Document(openapi={self.openapi}, info=Info(title={self.info.title}, version={self.info.version}), ...)'
