from quran.repository.models.image import Image
from quran.domain.image import Image as ImageDomain
from quran.utils.generate_key import generate_key


class ImageRepo:

    def create(self, image):
        image = Image.from_dict(image.to_dict())
        image.save()
        return ImageDomain.from_dict(image.to_dict())

    def find_by_ayah_id(self, ayah_id):
        key = generate_key(Image, ayah_id)
        image = Image.collection.get(key)
        if image:
            return ImageDomain.from_dict(image.to_dict())
        return None