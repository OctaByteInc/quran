class FindSurah:

    def __init__(self, surah_repo):
        self.surah_repo = surah_repo

    def by_id(self, id):
        return self.surah_repo.find_by_id(id)

    def by_number(self, number):
        return self.surah_repo.find_by_number(number)

    def by_name(self, name):
        return self.surah_repo.find_by_name(name)

    def by_english_name(self, english_name):
        return self.surah_repo.find_by_english_name(english_name)

    def by_revelation_type(self, revelation_type):
        return self.surah_repo.find_by_revelation_type(revelation_type)
