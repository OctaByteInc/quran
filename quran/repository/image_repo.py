from quran.repository.models.image import Image
from quran.domain.image import Image as ImageDomain
from quran.repository.repo_responses import ImageResponse
from quran.utils.generate_key import generate_key


class ImageRepo:

    def create(self, image):
        image = Image.from_dict(image.to_dict())
        image.save()
        return ImageResponse(image=ImageDomain.from_dict(image.to_dict()), number_of_results=1)

    def find_by_ayah_id(self, ayah_id):
        key = generate_key(Image, ayah_id)
        image = Image.collection.get(key)
        if image:
            return ImageResponse(image=ImageDomain.from_dict(image.to_dict()), number_of_results=1)
        return None