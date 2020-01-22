from quran.repository.image_repo import ImageRepo
from quran.usecase.image.create_image import CreateImage
from quran.usecase.image.find_image import FindImage


class ImageFactory:

    @classmethod
    def create(cls):
        image_repo = ImageRepo()
        return CreateImage(image_repo)

    @classmethod
    def find_image(cls):
        image_repo = ImageRepo()
        return FindImage(image_repo)
