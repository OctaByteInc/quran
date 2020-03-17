from quran.utils.response import Response


class FindAyah:

    def __init__(self, ayah_repo, find_translation, find_surah, find_edition, find_audio, find_image):
        self.ayah_repo = ayah_repo
        self.find_translation = find_translation
        self.find_surah = find_surah
        self.find_edition = find_edition
        self.find_audio = find_audio
        self.find_image = find_image

    def by_id(self, ayah_id, edition_id=None, parts=None):
        ayah = self.ayah_repo.find_by_id(ayah_id)
        return self._ayah_response(ayah, edition_id, parts)

    def by_surah_id(self, surah_id, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_surah_id(surah_id)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def by_number(self, ayah_number, edition_id=None, parts=None):
        ayah = self.ayah_repo.find_by_number(ayah_number)
        return self._ayah_response(ayah, edition_id, parts)

    def by_number_in_surah(self, number_in_surah, edition_id=None, parts=None):
        ayah = self.ayah_repo.find_by_number_in_surah(number_in_surah)
        return self._ayah_response(ayah, edition_id, parts)

    def by_juz(self, juz, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_juz(juz)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def by_manzil(self, manzil, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_manzil(manzil)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def by_ruku(self, ruku, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_ruku(ruku)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def by_hizb_quarter(self, hizb_quarter, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_hizb_quarter(hizb_quarter)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def by_sajda(self, sajda, edition_id=None, parts=None):
        ayah_stream = self.ayah_repo.find_by_sajda(sajda)
        for ayah in ayah_stream:
            yield self._ayah_response(ayah, edition_id, parts)

    def _ayah_response(self, ayah, edition_id, parts):
        response = Response()
        response.ayah = ayah

        if parts:
            surah_id = ayah.surah_id
            self._get_ayah_parts(response, parts, ayah.id, edition_id, surah_id)

        return response

    def _get_ayah_parts(self, response, parts, ayah_id, edition_id='edition-id-1', surah_id=None):
        # parts = ['Translation', 'Surah', 'Edition', 'Arabic_Audio', 'Translation_Audio', 'Image']

        if 'Translation' in parts:
            translation = self.find_translation.filter(ayah_id=ayah_id, edition_id=edition_id)
            response.translation = translation
        if 'Surah' in parts:
            if surah_id is None:
                ayah = self.ayah_repo.find_by_id(ayah_id)
                surah_id = ayah.surah_id
            surah = self.find_surah.by_id(surah_id)
            response.surah = surah
        if 'Edition' in parts:
            edition = self.find_edition.by_id(edition_id)
            response.edition = edition
        if 'Arabic_Audio' in parts:
            arabic_audio = self.find_audio.arabic_audio(ayah_id=ayah_id, edition_id=edition_id)
            response.arabic_audio = arabic_audio
        if 'Translation_Audio' in parts:
            translation_audio = self.find_audio.translation_audio(ayah_id=ayah_id, edition_id=edition_id)
            response.translation_audio = translation_audio
        if 'Image' in parts:
            image = self.find_image.by_ayah_id(ayah_id)
            response.ayah_image = image