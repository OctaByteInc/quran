from quran.repository.models.image import Image
from quran.domain.image import Image as ImageDomain
from quran.utils.generate_key import generate_key


class ImageRepo:

    def __init__(self):
        self.data = [
            {
                'ayah_id': 'ayah-id-1',
                'image': 'image url for ayah 1'
            },
            {
                'ayah_id': 'ayah-id-2',
                'image': 'image url for ayah 2'
            },
            {
                'ayah_id': 'ayah-id-3',
                'image': 'image url for ayah 3'
            },
        ]

    def create(self, image):
        self.data.append(image.to_dict())
        return ImageDomain.from_dict(image.to_dict())

    def find_by_ayah_id(self, ayah_id):
        for image in self.data:
            if image['id'] == ayah_id:
                return ImageDomain.from_dict(image)