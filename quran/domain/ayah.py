from dataclasses import dataclass

from quran.domain.entity import Entity


@dataclass
class Ayah(Entity):
    id: str
    surah_id: str
    number: int
    number_in_surah: int
    juz: int
    manzil: int
    ruku: int
    hizb_quarter: int
    sajda: bool
    arabic: str
