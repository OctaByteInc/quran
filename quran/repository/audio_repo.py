from quran.repository.models.audio import Audio
from quran.domain.audio import Audio as AudioDomain
from quran.utils.generate_key import generate_key


class AudioRepo:

    def create(self, audio):
        audio = Audio.from_dict(audio.to_dict())
        audio.save()
        return AudioDomain.from_dict(audio.to_dict())

    def find_by_id(self, id):
        key = generate_key(Audio, id)
        audio = Audio.collection.get(key)
        return AudioDomain.from_dict(audio.to_dict())

    def find_by_ayah_id(self, id):
        audio_stream = Audio.collection.filter(ayah_id=id).fetch()
        for audio in audio_stream:
            yield AudioDomain.from_dict(audio.to_dict())

    def find_by_edition_id(self, id):
        audio_stream = Audio.collection.filter(edition_id=id).fetch()
        for audio in audio_stream:
            yield AudioDomain.from_dict(audio.to_dict())