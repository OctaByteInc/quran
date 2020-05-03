class FindSurah:

    def __init__(self, surah_repo):
        self.surah_repo = surah_repo

    def get_all(self, limit=None, cursor=None):
        return self.surah_repo.get_all(limit=limit, cursor=cursor)

    def by_id(self, id):
        return self.surah_repo.find_by_id(id)

    def by_number(self, number):
        return self.surah_repo.find_by_number(number)

    def by_name(self, name):
        return self.surah_repo.find_by_name(name)

    def by_english_name(self, english_name):
        return self.surah_repo.find_by_english_name(english_name)

    def by_english_name_translation(self, english_name_translation):
        return self.surah_repo.find_by_english_name_translation(english_name_translation)

    def by_revelation_type(self, revelation_type, limit=None, cursor=None):
        return self.surah_repo.find_by_revelation_type(revelation_type, limit=limit, cursor=cursor)
