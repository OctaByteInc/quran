from quran.factory.audio_factory import AudioFactory
from quran.factory.edition_factory import EditionFactory
from quran.factory.surah_factory import SurahFactory
from quran.factory.translation_factory import TranslationFactory


class FindAyah:

    def __init__(self, ayah_repo):
        self.ayah_repo = ayah_repo

    def by_id(self, ayah_id, edition_id='en', parts=None):
        if not parts:
            parts = ['Ayah', 'Translation', 'Surah', 'Edition', 'Arabic_Audio', 'Translation_Audio', 'Image']

        surah_id = None

        if 'Ayah' in parts:
            ayah = self.ayah_repo.find_by_id(ayah_id)
            surah_id = ayah.surah_id
        if 'Translation' in parts:
            find_translation = TranslationFactory.find_translation()
            translation = find_translation.filter(ayah_id=ayah_id, edition_id=edition_id)
        if 'Surah' in parts:
            find_surah = SurahFactory.find_surah()
            if surah_id is None:
                ayah = self.ayah_repo.find_by_id(ayah_id)
                surah_id = ayah.surah_id
            surah = find_surah.by_id(surah_id)
        if 'Edition' in parts:
            find_edition = EditionFactory.find_edition()
            edition = find_edition.by_id(edition_id)
        if 'Arabic_Audio' in parts:
            find_audio = AudioFactory.find_audio()
            arabic_audio = find_audio.arabic_audio(ayah_id=ayah_id, edition_id=edition_id)
        if 'Translation_Audio' in parts:
            find_audio = AudioFactory.find_audio()
            arabic_audio = find_audio.translation_audio(ayah_id=ayah_id, edition_id=edition_id)
        if 'Image'



    def by_number(self, ayah_number):
        return self.ayah_repo.find_by_number(ayah_number)

    def by_number_in_surah(self, number_in_surah):
        return self.ayah_repo.find_by_number_in_surah(number_in_surah)

    def by_juz(self, juz):
        return self.ayah_repo.find_by_juz(juz)

    def by_manzil(self, manzil):
        return self.ayah_repo.find_by_manzil(manzil)

    def by_ruku(self, ruku):
        return self.ayah_repo.find_by_ruku(ruku)

    def by_hizb_quarter(self, hizb_quarter):
        return self.ayah_repo.find_by_hizb_quarter(hizb_quarter)

    def by_sajda(self, sajda):
        return self.ayah_repo.find_by_sajda(sajda)