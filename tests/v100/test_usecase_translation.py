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
    translation = find_translation.by_id('trans-id-3')

    assert translation.id == 'trans-id-3'


def test_find_translation_by_ayah_id():
    find_translation = TranslationFactory.find_translation()
    translation_stream = find_translation.by_ayah_id('ayah-id-2')
    translation = next(translation_stream)

    assert translation.ayah_id == 'ayah-id-2'


def test_find_translation_by_edition_id():
    find_translation = TranslationFactory.find_translation()
    translation_stream = find_translation.by_edition_id('edition-id-1')
    translation = next(translation_stream)

    assert translation.edition_id == 'edition-id-1'


def test_translation_filter():
    find_translation = TranslationFactory.find_translation()
    translation = find_translation.filter(ayah_id='ayah-id-2', edition_id='edition-id-1')

    assert translation.ayah_id == 'ayah-id-2'
    assert translation.edition_id == 'edition-id-1'