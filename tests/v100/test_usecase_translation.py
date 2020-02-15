from quran.domain.translation import Translation
from tests.quran.factory.translation_factory import TranslationFactory


def test_create_translation():
    data = {
        'id': 'trans-id-4',
        'ayah_id': 'ayah-id-2',
        'edition_id': 'edition-id-1',
        'text': 'Translation Text ayah_2 edition_1'
    }
    translation = Translation.from_dict(data)
    create_translation = TranslationFactory.create()
    translation = create_translation.exec(translation)

    assert translation.to_dict() == data


def test_find_translation_by_id():
    find_translation = TranslationFactory.find_translation()
    response = find_translation.by_id('trans-id-3')

    assert response.translation.id == 'trans-id-3'


def test_find_translation_by_ayah_id():
    find_translation = TranslationFactory.find_translation()
    response_stream = find_translation.by_ayah_id('ayah-id-2')
    translation = next(response_stream.translation)

    assert translation.ayah_id == 'ayah-id-2'


def test_find_translation_by_edition_id():
    find_translation = TranslationFactory.find_translation()
    response_stream = find_translation.by_edition_id('edition-id-1')
    translation = next(response_stream.translation)

    assert translation.edition_id == 'edition-id-1'


def test_translation_filter():
    find_translation = TranslationFactory.find_translation()
    response = find_translation.filter(ayah_id='ayah-id-2', edition_id='edition-id-1')

    assert response.translation.ayah_id == 'ayah-id-2'
    assert response.translation.edition_id == 'edition-id-1'