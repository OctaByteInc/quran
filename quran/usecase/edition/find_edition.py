from quran.utils.response import Response


class FindEdition:

    def __init__(self, edition_repo):
        self.edition_repo = edition_repo

    def by_id(self, id):
        edition = self.edition_repo.find_by_id(id)
        return self._edition_response(edition)

    def by_language(self, language):
        edition = self.edition_repo.find_by_language(language)
        return self._edition_response(edition)

    def by_name(self, name):
        edition = self.edition_repo.find_by_name(name)
        return self._edition_response(edition)

    def by_english_name(self, english_name):
        edition = self.edition_repo.find_by_english_name(english_name)
        return self._edition_response(edition)

    def by_type(self, type):
        edition = self.edition_repo.find_by_type(type)
        return self._edition_response(edition)

    def by_format(self, format):
        edition = self.edition_repo.find_by_format(format)
        return self._edition_response(edition)

    def _edition_response(self, edition):
        response = Response()
        response.edition = edition
        return response
