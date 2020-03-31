from quran.repository.models.translation import Translation
from quran.domain.translation import Translation as TranslationDomain
from quran.repository.repo_responses import TranslationResponse
from quran.utils.generate_key import generate_key


class TranslationRepo:

    def create(self, translation):
        translation = Translation.from_dict(translation.to_dict())
        translation.save()
        return TranslationResponse(translation=TranslationDomain.from_dict(translation.to_dict()), number_of_results=1)

    def find_by_id(self, id):
        key = generate_key(Translation, id)
        translation = Translation.collection.get(key)
        if translation:
            return TranslationResponse(translation=TranslationDomain.from_dict(translation.to_dict()),
                                       number_of_results=1)
        return None

    def find_by_ayah_id(self, ayah_id, limit=None, cursor=None):
        if cursor:
            translation_stream = Translation.collection.cursor(cursor).fetch(limit)
        else:
            translation_stream = Translation.collection.filter(ayah_id=ayah_id).fetch(limit)

        translation_list = []
        for translation in translation_stream:
            translation_list.append(TranslationDomain.from_dict(translation.to_dict()))

        return TranslationResponse(translation_list=translation_list, number_of_results=len(translation_list),
                                   cursor=translation_stream.cursor)

    def find_by_edition_id(self, edition_id, limit=None, cursor=None):
        if cursor:
            translation_stream = Translation.collection.cursor(cursor).fetch(limit)
        else:
            translation_stream = Translation.collection.filter(edition_id=edition_id).order('ayah_number').fetch(limit)

        translation_list = []
        for translation in translation_stream:
            translation_list.append(TranslationDomain.from_dict(translation.to_dict()))

        return TranslationResponse(translation_list=translation_list, number_of_results=len(translation_list),
                                   cursor=translation_stream.cursor)

    def filter(self, **kwargs):
        translation = Translation.collection.filter(**kwargs).get()
        if translation:
            return TranslationResponse(translation=TranslationDomain.from_dict(translation.to_dict()),
                                       number_of_results=1)
        return None
