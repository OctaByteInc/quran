from quran.repository.models.edition import Edition
from quran.domain.edition import Edition as EditionDomain
from quran.utils.generate_key import generate_key


class EditionRepo:

    def create(self, edition):
        edition = Edition.from_dict(edition.to_dict())
        edition.save()
        return EditionDomain.from_dict(edition.to_dict())

    def find_by_id(self, id):
        key = generate_key(Edition, id)
        edition = Edition.collection.get(key)
        return EditionDomain.from_dict(edition.to_dict())

    def find_by_language(self, language):
        edition_stream = Edition.collection.filter(language=language).fetch()
        for edition in edition_stream:
            return EditionDomain.from_dict(edition.to_dict())

    def find_by_name(self, name):
        edition_stream = Edition.collection.filter(name=name).fetch()
        for edition in edition_stream:
            return EditionDomain.from_dict(edition.to_dict())

    def find_by_english_name(self, name):
        edition_stream = Edition.collection.filter(english_name=name).fetch()
        for edition in edition_stream:
            return EditionDomain.from_dict(edition.to_dict())

    def find_by_type(self, type):
        edition_stream = Edition.collection.filter(type=type).fetch()
        for edition in edition_stream:
            return EditionDomain.from_dict(edition.to_dict())

    def find_by_format(self, format):
        edition_stream = Edition.collection.filter(format=format).fetch()
        for edition in edition_stream:
            return EditionDomain.from_dict(edition.to_dict())