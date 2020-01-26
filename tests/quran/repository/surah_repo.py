from quran.repository.models.surah import Surah
from quran.domain.surah import Surah as SurahDomain
from quran.utils.generate_key import generate_key


class SurahRepo:

    def __init__(self):
        self.data = [
            {
                'id': 'id_1',
                'number': 1,
                'name': 'surah name',
                'english_name': 'surah english name',
                'english_name_translation': 'english name translation',
                'number_of_ayahs': 10,
                'revelation_type': 'type-1'
            },
            {
                'id': 'id_2',
                'number': 2,
                'name': 'surah name',
                'english_name': 'surah english name',
                'english_name_translation': 'english name translation',
                'number_of_ayahs': 20,
                'revelation_type': 'type-2'
            },
        ]

    def create(self, surah):
        self.data.append(surah.to_dict())
        return SurahDomain.from_dict(surah.to_dict())

    def find_by_id(self, id):
        for surah in self.data:
            if surah['id'] == id:
                return SurahDomain.from_dict(surah)

    def find_by_number(self, number):
        for surah in self.data:
            if surah['number'] == number:
                return SurahDomain.from_dict(surah)

    def find_by_name(self, name):
        for surah in self.data:
            if surah['name'] == name:
                return SurahDomain.from_dict(surah)

    def find_by_english_name(self, english_name):
        for surah in self.data:
            if surah['english_name'] == english_name:
                return SurahDomain.from_dict(surah)

    def find_by_revelation_type(self, type):
        for surah in self.data:
            if surah['type'] == type:
                yield SurahDomain.from_dict(surah)