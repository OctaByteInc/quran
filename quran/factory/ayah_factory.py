from quran.repository.ayah_repo import AyahRepo
from quran.usecase.ayah.create_ayah import CreateAyah
from quran.usecase.ayah.find_ayah import FindAyah


class AyahFactory:

    @classmethod
    def create(cls):
        ayah_repo = AyahRepo()
        return CreateAyah(ayah_repo)

    @classmethod
    def find_ayah(cls):
        ayah_repo = AyahRepo()
        return FindAyah(ayah_repo)
