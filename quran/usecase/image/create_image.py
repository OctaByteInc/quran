class CreateImage:

    def __init__(self, image_repo):
        self.image_repo = image_repo

    def exec(self, image):
        return self.image_repo.create(image)
