class CreateTranslation:

    def __init__(self, translation_repo):
        self.translation_repo = translation_repo

    def exec(self, translation):
        return self.translation_repo.create(translation)
