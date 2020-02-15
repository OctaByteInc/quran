from quran.utils.response import Response


class FindSurah:

    def __init__(self, surah_repo):
        self.surah_repo = surah_repo

    def get_all(self):
        surah = self.surah_repo.get_all()
        return self._surah_response(surah)

    def by_id(self, id):
        surah = self.surah_repo.find_by_id(id)
        return self._surah_response(surah)

    def by_number(self, number):
        surah = self.surah_repo.find_by_number(number)
        return self._surah_response(surah)

    def by_name(self, name):
        surah = self.surah_repo.find_by_name(name)
        return self._surah_response(surah)

    def by_english_name(self, english_name):
        surah = self.surah_repo.find_by_english_name(english_name)
        return self._surah_response(surah)

    def by_revelation_type(self, revelation_type):
        surah = self.surah_repo.find_by_revelation_type(revelation_type)
        return self._surah_response(surah)

    def _surah_response(self, surah):
        response = Response()
        response.surah = surah
        return response
