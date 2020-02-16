from quran.domain.edition import Edition
from tests.quran.factory.edition_factory import EditionFactory


def test_craete_edition():
    data = {
        'id': 'edition-id-5',
        'language': 'ur',
        'name': 'Edition Name',
        'english_name': 'Edition English Name',
        'type': 'Translation',
        'format': 'format-5',
        'direction': 'rtl'
    }
    edition = Edition.from_dict(data)
    create_edition = EditionFactory.create()
    edition = create_edition.exec(edition)

    assert edition.to_dict() == data


def test_get_all_edition():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.get_all()
    edition = next(edition_stream)

    assert edition.id == 'edition-id-1'


def test_find_edition_by_id():
    find_edition = EditionFactory.find_edition()
    edition = find_edition.by_id('edition-id-4')

    assert edition.id == 'edition-id-4'
    assert edition.language == 'ur'


def test_find_edition_by_language():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.by_language('ur')
    edition = next(edition_stream)

    assert edition.language == 'ur'


def test_find_edition_by_name():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.by_name('Edition Name')
    edition = next(edition_stream)

    assert edition.name == 'Edition Name'


def test_find_edition_by_english_name():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.by_english_name('Edition English Name')
    edition = next(edition_stream)

    assert edition.english_name == 'Edition English Name'


def test_find_edition_by_type():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.by_type('Translation')
    edition = next(edition_stream)

    assert edition.type == 'Translation'


def test_find_edition_by_format():
    find_edition = EditionFactory.find_edition()
    edition_stream = find_edition.by_format('format-1')
    edition = next(edition_stream)

    assert edition.format == 'format-1'
