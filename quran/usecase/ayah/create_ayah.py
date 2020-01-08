class CreateAyah:

    def __init__(self, ayah_repo):
        self.ayah_repo = ayah_repo

    def exec(self, ayah):
        return self.ayah_repo.create(ayah)
