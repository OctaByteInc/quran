from quran.repository.models.translation import Translation
from quran.domain.translation import Translation as TranslationDomain
from quran.utils.generate_key import generate_key


class TranslationRepo:

    def __init__(self):
        self.data = [
            {
                'id': 'trans-id-1',
                'ayah_id': 'ayah-id-1',
                'edition_id': 'edition-id-1',
                'text': 'Translation Text for ayah_1 edition_1'
            },
            {
                'id': 'trans-id-2',
                'ayah_id': 'ayah-id-1',
                'edition_id': 'edition-id-2',
                'text': 'Translation Text ayah_1 edition_2'
            },
            {
                'id': 'trans-id-3',
                'ayah_id': 'ayah-id-2',
                'edition_id': 'edition-id-1',
                'text': 'Translation Text ayah_2 edition_1'
            }
        ]

    def create(self, translation):
        self.data.append(translation.to_dict())
        return TranslationDomain.from_dict(translation.to_dict())

    def find_by_id(self, id):
        for translation in self.data:
            if translation['id'] == id:
                return TranslationDomain.from_dict(translation)

    def find_by_ayah_id(self, ayah_id):
        for translation in self.data:
            if translation['ayah_id'] == ayah_id:
                yield TranslationDomain.from_dict(translation)

    def find_by_edition_id(self, edition_id):
        for translation in self.data:
            if translation['edition_id'] == edition_id:
                yield TranslationDomain.from_dict(translation)

    def filter(self, **kwargs):
        for translation in self.data:
            if translation['ayah_id'] == kwargs.get('ayah_id')\
                    and translation['edition_id'] == kwargs.get('edition_id'):
                return TranslationDomain.from_dict(translation)