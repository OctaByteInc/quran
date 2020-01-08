class CreateAudio:

    def __init__(self, audio_repo):
        self.audio_repo = audio_repo

    def exec(self, audio):
        return self.audio_repo.create(audio)
