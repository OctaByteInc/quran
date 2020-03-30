from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Audio(Entity):
    id: str
    ayah_id: str
    ayah_number: int
    edition_id: str
    type: str  # Translation or Arabic
    audio: str
