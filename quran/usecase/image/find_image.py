class FindImage:

    def __init__(self, image_repo):
        self.image_repo = image_repo

    def by_ayah_id(self, ayah_id):
        return self.image_repo.find_by_ayah_id(ayah_id)
