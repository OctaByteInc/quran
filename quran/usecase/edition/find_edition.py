class FindEdition:

    def __init__(self, edition_repo):
        self.edition_repo = edition_repo

    def by_id(self, id):
        return self.edition_repo.find_by_id(id)

    def by_language(self, language):
        return self.edition_repo.find_by_language(language)

    def by_name(self, name):
        return self.edition_repo.find_by_name(name)

    def by_english_name(self, english_name):
        return self.edition_repo.find_by_english_name(english_name)

    def by_type(self, type):
        return self.edition_repo.find_by_type(type)

    def by_format(self, format):
        return self.edition_repo.find_by_format(format)
