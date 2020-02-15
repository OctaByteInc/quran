from quran.domain.image import Image
from tests.quran.factory.image_factory import ImageFactory


def test_create_image():
    data = {
        'ayah_id': 'ayah-id-4',
        'image': 'image url for ayah 4'
    }
    image = Image.from_dict(data)
    create_image = ImageFactory.create()
    image = create_image.exec(image)

    assert image.to_dict() == data


def test_find_image_by_ayah_id():
    find_image = ImageFactory.find_image()
    response = find_image.by_ayah_id('ayah-id-3')

    assert response.image.ayah_id == 'ayah-id-3'
