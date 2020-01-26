from tests.quran.repository.edition_repo import EditionRepo
from quran.usecase.edition.create_edition import CreateEdition
from quran.usecase.edition.find_edition import FindEdition


class EditionFactory:

    @classmethod
    def create(cls):
        edition_repo = EditionRepo()
        return CreateEdition(edition_repo)

    @classmethod
    def find_edition(cls):
        edition_repo = EditionRepo()
        return FindEdition(edition_repo)
