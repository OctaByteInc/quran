from quran.domain.ayah import Ayah
from tests.quran.factory.ayah_factory import AyahFactory


def test_create_ayah():
    data = {
        'id': 'ayah-id-5',
        'surah_id': 'surah-id-2',
        'number': 3,
        'number_in_surah': 2,
        'juz': 2,
        'manzil': 2,
        'ruku': 2,
        'hizb_quarter': 2,
        'sajda': True,
        'arabic': 'Arabic Text of Ayah # 5'
    }

    ayah = Ayah.from_dict(data)
    create_ayah = AyahFactory.create()
    ayah = create_ayah.exec(ayah)

    assert data == ayah.to_dict()


def test_find_ayah_by_id():
    find_ayah = AyahFactory.find_ayah()
    response = find_ayah.by_id('ayah-id-1')

    assert response.ayah.id == 'ayah-id-1'


def test_find_ayah_by_number():
    find_ayah = AyahFactory.find_ayah()
    response = find_ayah.by_number(1)

    assert response.ayah.id == 'ayah-id-1'
    assert response.ayah.number == 1


def test_find_ayah_by_number_in_surah():
    find_ayah = AyahFactory.find_ayah()
    response = find_ayah.by_number_in_surah(1)

    assert response.ayah.id == 'ayah-id-1'


def test_find_ayah_by_juz():
    find_ayah = AyahFactory.find_ayah()
    ayah_stream = find_ayah.by_juz(1)
    response = next(ayah_stream)

    assert response.ayah.juz == 1


def test_find_ayah_by_manzil():
    find_ayah = AyahFactory.find_ayah()
    ayah_stream = find_ayah.by_manzil(1)
    response = next(ayah_stream)

    assert response.ayah.manzil == 1


def test_find_ayah_by_ruku():
    find_ayah = AyahFactory.find_ayah()
    ayah_stream = find_ayah.by_ruku(1)
    response = next(ayah_stream)

    assert response.ayah.ruku == 1


def test_find_ayah_by_hizb_quarter():
    find_ayah = AyahFactory.find_ayah()
    ayah_stream = find_ayah.by_hizb_quarter(1)
    response = next(ayah_stream)

    assert response.ayah.hizb_quarter == 1


def test_find_ayah_by_sajda():
    find_ayah = AyahFactory.find_ayah()
    ayah_stream = find_ayah.by_sajda(True)
    response = next(ayah_stream)

    assert response.ayah.sajda == True


def test_find_ayah_parts_by_id():
    find_ayah = AyahFactory.find_ayah()
    response = find_ayah.by_id('ayah-id-1', 'en',
                           ['Translation', 'Surah', 'Edition', 'Arabic_Audio', 'Translation_Audio', 'Image'])

    assert response.ayah.id == 'ayah-id-1'
    assert response.translation.edition_id == 'edition-id-1'
    assert response.translation.text == 'Translation Text for ayah_1 edition_1'

    assert response.surah.id == 'surah-id-1'
    assert response.surah.number == 1
    assert response.surah.revelation_type == 'type-1'

    assert response.edition.id == 'edition-id-1'
    assert response.edition.type == 'Audio'
    assert response.edition.format == 'format-1'

    assert response.arabic_audio.ayah_id == 'ayah-id-1'
    assert response.arabic_audio.edition_id == 'edition-id-1'
    assert response.arabic_audio.type == 'Arabic'
    assert response.arabic_audio.audio == 'Link to audio file for ayah id 1'

    assert ayah.translation_audio.ayah_id == 'ayah-id-1'
    assert ayah.translation_audio.edition_id == 'edition-id-1'
    assert ayah.translation_audio.type == 'Translation'
    assert ayah.translation_audio.audio == 'Link to Translation audio file for ayah id 1'

    assert ayah.ayah_image.ayah_id == 'ayah-id-1'
    assert ayah.ayah_image.image == 'image url for ayah 1'
