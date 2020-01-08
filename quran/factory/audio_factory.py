from quran.repository.audio_repo import AudioRepo
from quran.usecase.audio.create_audio import CreateAudio
from quran.usecase.audio.find_audio import FindAudio


class AudioFactory:

    @classmethod
    def create_audio(cls):
        audio_repo = AudioRepo()
        return CreateAudio(audio_repo)

    @classmethod
    def find_audio(cls):
        audio_repo = AudioRepo()
        return FindAudio(audio_repo)
