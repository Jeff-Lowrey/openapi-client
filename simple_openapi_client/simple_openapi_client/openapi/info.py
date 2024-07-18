from dataclasses import dataclass
from typing import Dict, List


@dataclass
class License:
    name: str
    url: str = None


@dataclass
class Contact:
    name: str = None
    url: str = None
    email: str = None


@dataclass
class Info:
    title: str
    version: str

    description: str = None
    termsOfServices: str = None
    contact: Contact = None
    license: License = None


@dataclass
class Tags:
    description: str = None
    schema: List[Dict[str, str]] = None
