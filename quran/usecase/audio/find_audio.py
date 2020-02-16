from quran.utils.allowed_filters import allowed_filters


class FindAudio:

    def __init__(self, audio_repo):
        self.audio_repo = audio_repo

    def by_id(self, id):
        return self.audio_repo.find_by_id(id)

    def by_ayah_id(self, ayah_id):
        return self.audio_repo.find_by_ayah_id(ayah_id)

    def by_edition_id(self, edition_id):
        return self.audio_repo.find_by_edition_id(edition_id)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def arabic_audio(self, **kwargs):
        return self.audio_repo.find_arabic_audio(**kwargs)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def translation_audio(self, **kwargs):
        return self.audio_repo.find_translation_audio(**kwargs)

