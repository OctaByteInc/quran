from quran.utils.allowed_filters import allowed_filters
from quran.utils.response import Response


class FindAudio:

    def __init__(self, audio_repo):
        self.audio_repo = audio_repo

    def by_id(self, id):
        audio = self.audio_repo.find_by_id(id)
        return self._audio_response(audio)

    def by_ayah_id(self, ayah_id):
        audio = self.audio_repo.find_by_ayah_id(ayah_id)
        return self._audio_response(audio)

    def by_edition_id(self, edition_id):
        audio = self.audio_repo.find_by_edition_id(edition_id)
        return self._audio_response(audio)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def arabic_audio(self, **kwargs):
        audio = self.audio_repo.find_arabic_audio(**kwargs)
        return self._audio_response(audio)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def translation_audio(self, **kwargs):
        audio = self.audio_repo.find_translation_audio(**kwargs)
        return self._audio_response(audio)

    def _audio_response(self, audio):
        response = Response()
        response.audio  = audio
        return response
