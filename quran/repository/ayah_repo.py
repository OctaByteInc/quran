from quran.repository.models.ayah import Ayah
from quran.domain.ayah import Ayah as AyahDomain
from quran.repository.repo_responses import AyahResponse
from quran.utils.generate_key import generate_key


class AyahRepo:

    def create(self, ayah):
        ayah = Ayah.from_dict(ayah.to_dict())
        ayah.save()
        return AyahResponse(ayah=AyahDomain.from_dict(ayah.to_dict()), number_of_results=1)

    def find_by_id(self, id):
        key = generate_key(Ayah, id)
        ayah = Ayah.collection.get(key)
        if ayah:
            return AyahResponse(ayah=AyahDomain.from_dict(ayah.to_dict()), number_of_results=1)
        return None

    def find_by_surah_id(self, surah_id, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.cursor(cursor).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(surah_id=surah_id).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)

    def find_by_number(self, number):
        ayah = Ayah.collection.filter(number=number).get()
        if ayah:
            return AyahResponse(ayah=AyahDomain.from_dict(ayah.to_dict()), number_of_results=1)
        return None

    def find_by_number_in_surah(self, number):
        ayah = Ayah.collection.filter(number_in_surah=number).get()
        if ayah:
            return AyahResponse(ayah=AyahDomain.from_dict(ayah.to_dict()), number_of_results=1)
        return None

    def find_by_juz(self, juz, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.cursor(cursor).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(juz=juz).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)

    def find_by_manzil(self, manzil, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.cursor(cursor).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(manzil=manzil).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)

    def find_by_ruku(self, ruku, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.filter(ruku=ruku).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(ruku=ruku).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)

    def find_by_hizb_quarter(self, hizb_quarter, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.cursor(cursor).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(hizb_quarter=hizb_quarter).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)

    def find_by_sajda(self, sajda, limit=None, cursor=None):
        if cursor:
            ayah_stream = Ayah.collection.filter(sajda=sajda).fetch(limit)
        else:
            ayah_stream = Ayah.collection.filter(sajda=sajda).fetch(limit)

        ayah_list = []
        for ayah in ayah_stream:
            ayah_list.append(AyahDomain.from_dict(ayah.to_dict()))

        return AyahResponse(ayah_list=ayah_list, number_of_results=len(ayah_list), cursor=ayah_stream.cursor)