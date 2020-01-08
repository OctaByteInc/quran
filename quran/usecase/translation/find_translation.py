from quran.utils.allowed_filters import allowed_filters


class FindTranslation:

    def __init__(self, translation_repo):
        self.translation_repo = translation_repo

    def by_id(self, id):
        return self.translation_repo.find_by_id(id)

    def by_ayah_id(self, ayah_id):
        return self.translation_repo.find_by_ayah_id(ayah_id)

    def by_edition_id(self, edition_id):
        return self.translation_repo.find_by_edition_id(edition_id)

    @allowed_filters(include=['ayah_id', 'edition_id'])
    def filter(self, **kwargs):
        return self.translation_repo.filter(**kwargs)
