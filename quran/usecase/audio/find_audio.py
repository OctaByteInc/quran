class FindAudio:

    def __init__(self, audio_repo):
        self.audio_repo = audio_repo

    def by_ayah_id(self, ayah_id):
        return self.audio_repo.find_by_ayah_id(ayah_id)

    def by_edition_id(self, edition_id):
        return self.audio_repo.find_by_edition_id(edition_id)
