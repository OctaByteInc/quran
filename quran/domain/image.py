from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Image(Entity):
    ayah_id: str
    image: str
