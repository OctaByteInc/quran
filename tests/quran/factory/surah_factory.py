from tests.quran.repository.surah_repo import SurahRepo
from quran.usecase.surah.create_surah import CreateSurah
from quran.usecase.surah.find_surah import FindSurah


class SurahFactory:

    @classmethod
    def create(cls):
        surah_repo = SurahRepo()
        return CreateSurah(surah_repo)

    @classmethod
    def find_surah(cls):
        surah_repo = SurahRepo()
        return FindSurah(surah_repo)
