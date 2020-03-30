from quran.repository.models.edition import Edition
from quran.domain.edition import Edition as EditionDomain
from quran.repository.repo_responses import EditionResponse
from quran.utils.generate_key import generate_key


class EditionRepo:

    def create(self, edition):
        edition = Edition.from_dict(edition.to_dict())
        edition.save()
        return EditionResponse(edition=EditionDomain.from_dict(edition.to_dict()), number_of_results=1)

    def get_all(self, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)

    def find_by_id(self, id):
        key = generate_key(Edition, id)
        edition = Edition.collection.get(key)
        if edition:
            return EditionResponse(edition=EditionDomain.from_dict(edition.to_dict()), number_of_results=1)
        return None

    def find_by_language(self, language, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.filter(language=language).fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)

    def find_by_name(self, name, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.filter(name=name).fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)

    def find_by_translator(self, translator, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.filter(translator=translator).fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)

    def find_by_type(self, type, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.filter(type=type).fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)

    def find_by_format(self, format, limit=None, cursor=None):
        if cursor:
            edition_stream = Edition.collection.cursor(cursor).fetch(limit)
        else:
            edition_stream = Edition.collection.filter(format=format).fetch(limit)

        edition_list = []
        for edition in edition_stream:
            edition_list.append(EditionDomain.from_dict(edition.to_dict()))

        return EditionResponse(edition_list=edition_list, number_of_results=len(edition_list),
                               cursor=edition_stream.cursor)
