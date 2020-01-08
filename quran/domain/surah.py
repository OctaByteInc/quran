from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Surah(Entity):
    id: str
    number: int
    name: str
    english_name: str
    english_name_translation: str
    number_of_ayahs: int
    revelation_type: str
