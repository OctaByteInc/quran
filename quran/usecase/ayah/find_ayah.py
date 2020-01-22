from quran.factory.audio_factory import AudioFactory
from quran.factory.edition_factory import EditionFactory
from quran.factory.image_factory import ImageFactory
from quran.factory.surah_factory import SurahFactory
from quran.factory.translation_factory import TranslationFactory
from quran.utils.response import Response


class FindAyah:

    def __init__(self, ayah_repo):
        self.ayah_repo = ayah_repo

    def by_id(self, ayah_id, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_id(ayah_id)
        return self._ayah_response(ayah, edition_id, parts)

    def by_number(self, ayah_number, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_number(ayah_number)
        return self._ayah_response(ayah, edition_id, parts)

    def by_number_in_surah(self, number_in_surah, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_number_in_surah(number_in_surah)
        return self._ayah_response(ayah, edition_id, parts)

    def by_juz(self, juz, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_juz(juz)
        return self._ayah_response(ayah, edition_id, parts)

    def by_manzil(self, manzil, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_manzil(manzil)
        return self._ayah_response(ayah, edition_id, parts)

    def by_ruku(self, ruku, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_ruku(ruku)
        return self._ayah_response(ayah, edition_id, parts)

    def by_hizb_quarter(self, hizb_quarter, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_hizb_quarter(hizb_quarter)
        return self._ayah_response(ayah, edition_id, parts)

    def by_sajda(self, sajda, edition_id='en', parts=None):
        ayah = self.ayah_repo.find_by_sajda(sajda)
        return self._ayah_response(ayah, edition_id, parts)

    def _ayah_response(self, ayah, edition_id, parts):
        response = Response()
        response.ayah = ayah

        if parts:
            surah_id = ayah.surah_id
            self._get_ayah_parts(parts, ayah.id, edition_id, surah_id)

        return response

    def _get_ayah_parts(self, parts, ayah_id, edition_id='en', surah_id=None):
        # parts = ['Translation', 'Surah', 'Edition', 'Arabic_Audio', 'Translation_Audio', 'Image']

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
        if 'Image':
            find_image = ImageFactory.find_image()
            ayah_image = find_image.by_ayah_id(ayah_id)