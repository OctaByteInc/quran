from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Audio(Entity):
    id: str
    ayah_id: str
    edition_id: str
    type: str
    audio: str
