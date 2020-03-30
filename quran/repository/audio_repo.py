from quran.repository.models.audio import Audio
from quran.domain.audio import Audio as AudioDomain
from quran.repository.repo_responses import AudioResponse
from quran.utils.generate_key import generate_key


class AudioRepo:

    def create(self, audio):
        audio = Audio.from_dict(audio.to_dict())
        audio.save()
        return AudioResponse(audio=AudioDomain.from_dict(audio.to_dict()), number_of_results=1)

    def find_by_id(self, id):
        key = generate_key(Audio, id)
        audio = Audio.collection.get(key)
        if audio:
            return AudioResponse(audio=AudioDomain.from_dict(audio.to_dict()), number_of_results=1)
        return None

    def find_by_ayah_id(self, id, limit=None, cursor=None):
        if cursor:
            audio_stream = Audio.collection.cursor(cursor).fetch(limit)
        else:
            audio_stream = Audio.collection.filter(ayah_id=id).fetch(limit)

        audio_list = []
        for audio in audio_stream:
            audio_list.append(AudioDomain.from_dict(audio.to_dict()))

        return AudioResponse(audio_list=audio_list, number_of_results=len(audio_list), cursor=audio_stream.cursor)

    def find_by_edition_id(self, id, limit=None, cursor=None):
        if cursor:
            audio_stream = Audio.collection.cursor(cursor).fetch(limit)
        else:
            audio_stream = Audio.collection.filter(edition_id=id).order('ayah_number').fetch(limit)

        audio_list = []
        for audio in audio_stream:
            audio_list.append(AudioDomain.from_dict(audio.to_dict()))

        AudioResponse(audio_list=audio_list, number_of_results=len(audio_list), cursor=audio_stream.cursor)

    def find_arabic_audio(self, **kwargs):
        audio = Audio.collection.filter(**kwargs).filter(type='Arabic').get()
        if audio:
            return AudioResponse(audio=AudioDomain.from_dict(audio.to_dict()), number_of_results=1)
        return None

    def find_translation_audio(self, **kwargs):
        audio = Audio.collection.filter(**kwargs).filter(type='Translation').get()
        if audio:
            return AudioResponse(audio=AudioDomain.from_dict(audio.to_dict()), number_of_results=1)
        return None