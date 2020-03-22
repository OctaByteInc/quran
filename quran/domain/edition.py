from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Edition(Entity):
    id: str
    language: str
    name: str
    translator: str
    type: str
    format: str
    direction: str
