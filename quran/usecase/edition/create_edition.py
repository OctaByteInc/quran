class CreateEdition:

    def __init__(self, edition_repo):
        self.edition_repo = edition_repo

    def exec(self, edition):
        return self.edition_repo.create(edition)
