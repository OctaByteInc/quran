from quran.domain.ayah import Ayah


def test_create_ayah_from_dict():
    a_dict = {'number': 1, 'id': '1-1', 'surah_id': 'surah-1', 'number_in_surah': 1, 'juz': 1, 'manzil': 1,
              'ruku': 1, 'hizb_quarter': 1, 'sajda': False, 'arabic': 'some arabic text'}

    ayah = Ayah.from_dict(a_dict)

    assert ayah.id == '1-1'
    assert ayah.sajda == False
    assert ayah.number == 1
