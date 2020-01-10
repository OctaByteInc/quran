from quran.repository.models.translation import Translation
from quran.domain.translation import Translation as TranslationDomain


class TranslationRepo:

    def create(self, translation):
        translation = Translation.from_dict(translation.to_dict())
        translation.save()
        return TranslationDomain.from_dict(translation.to_dict())