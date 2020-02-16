from quran.domain.ayah import Ayah as AyahDomain


class AyahRepo:

    def __init__(self):
        self.data = [
            {
                'id': 'ayah-id-1',
                'surah_id': 'surah-id-1',
                'number': 1,
                'number_in_surah': 1,
                'juz': 1,
                'manzil': 1,
                'ruku': 1,
                'hizb_quarter': 1,
                'sajda': False,
                'arabic': 'Arabic Text of Ayah # 1'
            },
            {
                'id': 'ayah-id-2',
                'surah_id': 'surah-id-1',
                'number': 2,
                'number_in_surah': 2,
                'juz': 1,
                'manzil': 1,
                'ruku': 1,
                'hizb_quarter': 1,
                'sajda': True,
                'arabic': 'Arabic Text of Ayah # 2'
            },
            {
                'id': 'ayah-id-3',
                'surah_id': 'surah-id-2',
                'number': 3,
                'number_in_surah': 2,
                'juz': 2,
                'manzil': 2,
                'ruku': 2,
                'hizb_quarter': 2,
                'sajda': False,
                'arabic': 'Arabic Text of Ayah # 3'
            },
            {
                'id': 'ayah-id-4',
                'surah_id': 'surah-id-2',
                'number': 3,
                'number_in_surah': 2,
                'juz': 2,
                'manzil': 2,
                'ruku': 2,
                'hizb_quarter': 2,
                'sajda': True,
                'arabic': 'Arabic Text of Ayah # 4'
            }
        ]

    def create(self, ayah):
        self.data.append(ayah.to_dict)
        return AyahDomain.from_dict(ayah.to_dict())

    def find_by_id(self, id):
        for ayah in self.data:
            if ayah['id'] == id:
                return AyahDomain.from_dict(ayah)

    def find_by_surah_id(self, surah_id):
        for ayah in self.data:
            if ayah['surah_id'] == surah_id:
                yield AyahDomain.from_dict(ayah)

    def find_by_number(self, number):
        for ayah in self.data:
            if ayah['number'] == number:
                return AyahDomain.from_dict(ayah)

    def find_by_number_in_surah(self, number):
        for ayah in self.data:
            if ayah['number_in_surah'] == number:
                return AyahDomain.from_dict(ayah)

    def find_by_juz(self, juz):
        for ayah in self.data:
            if ayah['juz'] == juz:
                yield AyahDomain.from_dict(ayah)

    def find_by_manzil(self, manzil):
        for ayah in self.data:
            if ayah['manzil'] == manzil:
                yield AyahDomain.from_dict(ayah)

    def find_by_ruku(self, ruku):
        for ayah in self.data:
            if ayah['ruku'] == ruku:
                yield AyahDomain.from_dict(ayah)

    def find_by_hizb_quarter(self, hizb_quarter):
        for ayah in self.data:
            if ayah['hizb_quarter'] == hizb_quarter:
                yield AyahDomain.from_dict(ayah)

    def find_by_sajda(self, sajda):
        for ayah in self.data:
            if ayah['sajda'] == sajda:
                yield AyahDomain.from_dict(ayah)