from quran.repository.models.ayah import Ayah
from quran.domain.ayah import Ayah as AyahDomain
from quran.utils.generate_key import generate_key


class AyahRepo:

    def create(self, ayah):
        ayah = Ayah.from_dict(ayah.to_dict())
        ayah.save()
        return AyahDomain.from_dict(ayah.to_dict())

    def find_by_id(self, id):
        key = generate_key(Ayah, id)
        ayah = Ayah.collection.get(key)
        return AyahDomain.from_dict(ayah.to_dict())

    def find_by_surah_id(self, surah_id):
        ayah_stream = Ayah.collection.filter(surah_id=surah_id).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())

    def find_by_number(self, number):
        ayah = Ayah.collection.filter(number=number).get()
        return AyahDomain.from_dict(ayah.to_dict())

    def find_by_number_in_surah(self, number):
        ayah = Ayah.collection.filter(number_in_surah=number).get()
        return AyahDomain.from_dict(ayah.to_dict())

    def find_by_juz(self, juz):
        ayah_stream = Ayah.collection.filter(juz=juz).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())

    def find_by_manzil(self, manzil):
        ayah_stream = Ayah.collection.filter(manzil=manzil).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())

    def find_by_ruku(self, ruku):
        ayah_stream = Ayah.collection.filter(ruku=ruku).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())

    def find_by_hizb_quarter(self, hizb_quarter):
        ayah_stream = Ayah.collection.filter(hizb_quarter=hizb_quarter).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())

    def find_by_sajda(self, sajda):
        ayah_stream = Ayah.collection.filter(sajda=sajda).fetch()
        for ayah in ayah_stream:
            yield AyahDomain.from_dict(ayah.to_dict())