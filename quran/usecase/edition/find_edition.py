class FindEdition:

    def __init__(self, edition_repo):
        self.edition_repo = edition_repo

    def get_all(self, limit=None, cursor=None):
        return self.edition_repo.get_all(limit=limit, cursor=cursor)

    def by_id(self, id):
        return self.edition_repo.find_by_id(id)

    def by_language(self, language, limit=None, cursor=None):
        return self.edition_repo.find_by_language(language, limit=limit, cursor=cursor)

    def by_name(self, name, limit=None, cursor=None):
        return self.edition_repo.find_by_name(name, limit=limit, cursor=cursor)

    def by_translator(self, translator, limit=None, cursor=None):
        return self.edition_repo.find_by_translator(translator, limit=limit, cursor=cursor)

    def by_type(self, type, limit=None, cursor=None):
        return self.edition_repo.find_by_type(type, limit=limit, cursor=cursor)

    def by_format(self, format, limit=None, cursor=None):
        return self.edition_repo.find_by_format(format, limit=limit, cursor=cursor)
