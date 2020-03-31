from quran.repository.repo_responses import AyahResponse
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
        ayah_res = self.ayah_repo.find_by_id(ayah_id)
        response = self._ayah_response(ayah_res.ayah, edition_id, parts)
        return AyahResponse(ayah=response, number_of_results=ayah_res.number_of_results)

    def by_surah_id(self, surah_id, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_surah_id(surah_id, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

    def by_number(self, ayah_number, edition_id=None, parts=None):
        ayah_res = self.ayah_repo.find_by_number(ayah_number)
        response = self._ayah_response(ayah_res.ayah, edition_id, parts)
        return AyahResponse(ayah=response, number_of_results=ayah_res.number_of_results)

    def by_number_in_surah(self, number_in_surah, edition_id=None, parts=None):
        ayah_res = self.ayah_repo.find_by_number_in_surah(number_in_surah)
        response = self._ayah_response(ayah_res.ayah, edition_id, parts)
        return AyahResponse(ayah=response, number_of_results=ayah_res.number_of_results)

    def by_juz(self, juz, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_juz(juz, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

    def by_manzil(self, manzil, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_manzil(manzil, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

    def by_ruku(self, ruku, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_ruku(ruku, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah_res in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah_res, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

    def by_hizb_quarter(self, hizb_quarter, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_hizb_quarter(hizb_quarter, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

    def by_sajda(self, sajda, edition_id=None, parts=None, limit=None, cursor=None):
        ayah_stream = self.ayah_repo.find_by_sajda(sajda, limit=limit, cursor=cursor)
        ayah_list = []
        for ayah in ayah_stream.ayah_list:
            ayah_list.append(self._ayah_response(ayah, edition_id, parts))

        return AyahResponse(ayah_list=ayah_list, number_of_results=ayah_stream.number_of_results,
                            cursor=ayah_stream.cursor)

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
            translation_res = self.find_translation.filter(ayah_id=ayah_id, edition_id=edition_id)
            if translation_res:
                response.translation = translation_res.translation
        if 'Surah' in parts:
            if surah_id is None:
                ayah_res = self.ayah_repo.find_by_id(ayah_id)
                surah_id = ayah_res.ayah.surah_id
            surah_res = self.find_surah.by_id(surah_id)
            if surah_res:
                response.surah = surah_res.surah
        if 'Edition' in parts:
            edition_res = self.find_edition.by_id(edition_id)
            if edition_res:
                response.edition = edition_res.edition
        if 'Arabic_Audio' in parts:
            arabic_audio = self.find_audio.arabic_audio(ayah_id=ayah_id, edition_id=edition_id)
            if arabic_audio:
                response.arabic_audio = arabic_audio.audio
        if 'Translation_Audio' in parts:
            translation_audio = self.find_audio.translation_audio(ayah_id=ayah_id, edition_id=edition_id)
            if translation_audio:
                response.translation_audio = translation_audio.audio
        if 'Image' in parts:
            image_res = self.find_image.by_ayah_id(ayah_id)
            if image_res:
                response.ayah_image = image_res.image
