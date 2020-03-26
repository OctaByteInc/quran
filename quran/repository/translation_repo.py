from quran.repository.models.translation import Translation
from quran.domain.translation import Translation as TranslationDomain
from quran.utils.generate_key import generate_key


class TranslationRepo:

    def create(self, translation):
        translation = Translation.from_dict(translation.to_dict())
        translation.save()
        return TranslationDomain.from_dict(translation.to_dict())

    def find_by_id(self, id):
        key = generate_key(Translation, id)
        translation = Translation.collection.get(key)
        return TranslationDomain.from_dict(translation.to_dict())

    def find_by_ayah_id(self, ayah_id):
        translation_stream = Translation.collection.filter(ayah_id=ayah_id).fetch()
        for translation in translation_stream:
            yield TranslationDomain.from_dict(translation.to_dict())

    def find_by_edition_id(self, edition_id):
        translation_steam = Translation.collection.filter(edition_id=edition_id).order('ayah_number').fetch()
        for translation in translation_steam:
            yield TranslationDomain.from_dict(translation.to_dict())

    def filter(self, **kwargs):
        translation = Translation.collection.filter(**kwargs).get()
        return TranslationDomain.from_dict(translation.to_dict())