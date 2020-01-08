class CreateSurah:

    def __init__(self, surah_repo):
        self.surah_repo = surah_repo

    def exec(self, surah):
        return self.surah_repo.create(surah)
