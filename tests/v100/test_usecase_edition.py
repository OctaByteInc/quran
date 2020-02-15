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


def test_find_edition_by_id():
    find_edition = EditionFactory.find_edition()
    response = find_edition.by_id('edition-id-4')

    assert response.edition.id == 'edition-id-4'
    assert response.edition.language == 'ur'


def test_find_edition_by_language():
    find_edition = EditionFactory.find_edition()
    response_stream = find_edition.by_language('ur')
    edition = next(response_stream.edition)

    assert edition.language == 'ur'


def test_find_edition_by_name():
    find_edition = EditionFactory.find_edition()
    response_stream = find_edition.by_name('Edition Name')
    edition = next(response_stream.edition)

    assert edition.name == 'Edition Name'


def test_find_edition_by_english_name():
    find_edition = EditionFactory.find_edition()
    response_stream = find_edition.by_english_name('Edition English Name')
    edition = next(response_stream.edition)

    assert edition.english_name == 'Edition English Name'


def test_find_edition_by_type():
    find_edition = EditionFactory.find_edition()
    response_stream = find_edition.by_type('Translation')
    edition = next(response_stream.edition)

    assert edition.type == 'Translation'


def test_find_edition_by_format():
    find_edition = EditionFactory.find_edition()
    response_stream = find_edition.by_format('format-1')
    edition = next(response_stream.edition)

    assert edition.format == 'format-1'
