from quran.repository.translation_repo import TranslationRepo
from quran.usecase.translation.create_translation import CreateTranslation
from quran.usecase.translation.find_translation import FindTranslation


class TranslationFactory:

    @classmethod
    def create(cls):
        translation_repo = TranslationRepo()
        return CreateTranslation(translation_repo)

    @classmethod
    def find_translation(cls):
        translation_repo = TranslationRepo()
        return FindTranslation(translation_repo)
