from quran.utils.allowed_filters import allowed_filters
from quran.utils.response import Response


class FindTranslation:

    def __init__(self, translation_repo):
        self.translation_repo = translation_repo

    def by_id(self, id):
        translation = self.translation_repo.find_by_id(id)
        return self._translation_response(translation)

    def by_ayah_id(self, ayah_id):
        translation = self.translation_repo.find_by_ayah_id(ayah_id)
        return self._translation_response(translation)

    def by_edition_id(self, edition_id):
        translation = self.translation_repo.find_by_edition_id(edition_id)
        return self._translation_response(translation)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def filter(self, **kwargs):
        translation = self.translation_repo.filter(**kwargs)
        return self._translation_response(translation)

    def _translation_response(self, translation):
        response = Response()
        response.translation = translation
        return response