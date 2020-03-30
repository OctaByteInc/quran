from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Translation(Entity):
    id: str
    ayah_id: str
    ayah_number: str
    edition_id: str
    text: str
