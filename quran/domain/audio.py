from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Audio(Entity):
    ayah_id: str
    edition_id: str
    audio: str
