from quran.repository.models.surah import Surah
from quran.domain.surah import Surah as SurahDomain
from quran.repository.repo_responses import SurahResponse
from quran.utils.generate_key import generate_key


class SurahRepo:

    def create(self, surah):
        surah = Surah.from_dict(surah.to_dict())
        surah.save()
        return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)

    def get_all(self, limit=None, cursor=None):
        if cursor:
            surah_stream = Surah.collection.cursor(cursor).fetch(limit)
        else:
            surah_stream = Surah.collection.fetch(limit)

        surah_list = []
        for surah in surah_stream:
            surah_list.append(SurahDomain.from_dict(surah.to_dict()))

        return SurahResponse(surah_list=surah_list, number_of_results=len(surah_list), cursor=surah_stream.cursor)

    def find_by_id(self, id):
        key = generate_key(Surah, id)
        surah = Surah.collection.get(key)
        if surah:
            return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)
        return None

    def find_by_number(self, number):
        surah = Surah.collection.filter(number=number).get()
        if surah:
            return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)
        return None

    def find_by_name(self, name):
        surah = Surah.collection.filter(name=name).get()
        if surah:
            return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)
        return None

    def find_by_english_name(self, english_name):
        surah = Surah.collection.filter(english_name=english_name).get()
        if surah:
            return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)
        return None

    def find_by_english_name_translation(self, english_name_translation):
        surah = Surah.collection.filter(english_name_translation=english_name_translation).get()
        if surah:
            return SurahResponse(surah=SurahDomain.from_dict(surah.to_dict()), number_of_results=1)
        return None

    def find_by_revelation_type(self, type, limit=None, cursor=None):
        if cursor:
            surah_stream = Surah.collection.cursor(cursor).fetch(limit)
        else:
            surah_stream = Surah.collection.filter(revelation_type=type).fetch(limit)

        surah_list = []
        for surah in surah_stream:
            surah_list.append(SurahDomain.from_dict(surah.to_dict()))

        return SurahResponse(surah_list=surah_list, number_of_results=len(surah_list), cursor=surah_stream.cursor)