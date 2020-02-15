from quran.domain.surah import Surah
from tests.quran.factory.surah_factory import SurahFactory


def test_create_surah():
    data = {
        'id': 'surah-id-3',
        'number': 3,
        'name': 'surah name',
        'english_name': 'surah english name',
        'english_name_translation': 'english name translation',
        'number_of_ayahs': 10,
        'revelation_type': 'type-1'
    }
    surah = Surah.from_dict(data)
    create_surah = SurahFactory.create()
    surah = create_surah.exec(surah)

    assert surah.to_dict() == data


def test_find_surah_by_id():
    find_surah = SurahFactory.find_surah()
    response = find_surah.by_id('surah-id-1')

    assert response.surah.id == 'surah-id-1'


def test_find_surah_by_number():
    find_surah = SurahFactory.find_surah()
    response = find_surah.by_number(1)

    assert response.surah.number == 1


def test_find_surah_by_name():
    find_surah = SurahFactory.find_surah()
    response = find_surah.by_name('surah name')

    assert response.surah.name == 'surah name'


def test_find_surah_by_english_name():
    find_surah = SurahFactory.find_surah()
    response = find_surah.by_english_name('surah english name')

    assert response.surah.english_name == 'surah english name'


def test_find_surah_by_revelation_type():
    find_surah = SurahFactory.find_surah()
    response_stream = find_surah.by_revelation_type('type-1')
    surah = next(response_stream.surah)

    assert surah.revelation_type == 'type-1'