from quran.factory.audio_factory import AudioFactory
from quran.factory.edition_factory import EditionFactory
from quran.factory.image_factory import ImageFactory
from quran.factory.surah_factory import SurahFactory
from quran.factory.translation_factory import TranslationFactory
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
        find_translation = TranslationFactory.find_translation()
        find_surah = SurahFactory.find_surah()
        find_edition = EditionFactory.find_edition()
        find_audio = AudioFactory.find_audio()
        find_image = ImageFactory.find_image()
        return FindAyah(ayah_repo, find_translation, find_surah, find_edition, find_audio, find_image)
