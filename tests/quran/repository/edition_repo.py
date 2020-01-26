from quran.repository.models.edition import Edition
from quran.domain.edition import Edition as EditionDomain
from quran.utils.generate_key import generate_key


class EditionRepo:

    def __init__(self):
        self.data = [
            {
                'id': 'id_1',
                'language': 'en',
                'name': 'Edition Name',
                'english_name': 'Edition English Name',
                'type': 'Audio',
                'format': 'format-1',
                'direction': 'ltr'
            },
            {
                'id': 'id_2',
                'language': 'en',
                'name': 'Edition Name',
                'english_name': 'Edition English Name',
                'type': 'Translation',
                'format': 'format-2',
                'direction': 'ltr'
            },
            {
                'id': 'id_3',
                'language': 'ur',
                'name': 'Edition Name',
                'english_name': 'Edition English Name',
                'type': 'Audio',
                'format': 'format-3',
                'direction': 'rtl'
            },
            {
                'id': 'id_4',
                'language': 'ur',
                'name': 'Edition Name',
                'english_name': 'Edition English Name',
                'type': 'Translation',
                'format': 'format-4',
                'direction': 'rtl'
            }
        ]

    def create(self, edition):
        self.data.append(edition.to_dict())
        return EditionDomain.from_dict(edition.to_dict())

    def find_by_id(self, id):
        for edition in self.data:
            if edition['id'] == id:
                return EditionDomain.from_dict(edition)

    def find_by_language(self, language):
        for edition in self.data:
            if edition['language'] == language:
                yield EditionDomain.from_dict(edition)

    def find_by_name(self, name):
        for edition in self.data:
            if edition['name'] == name:
                yield EditionDomain.from_dict(edition)

    def find_by_english_name(self, name):
        for edition in self.data:
            if edition['english_name'] == name:
                yield EditionDomain.from_dict(edition)

    def find_by_type(self, type):
        for edition in self.data:
            if edition['type'] == type:
                yield EditionDomain.from_dict(edition)

    def find_by_format(self, format):
        for edition in self.data:
            if edition['format'] == format:
                yield EditionDomain.from_dict(edition)