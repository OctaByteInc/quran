from quran.domain.ayah import Ayah


def test_create_ayah_object_from_dict():
    a_dict = {'id': '1-1'}
    ayah = Ayah(**a_dict)

    assert ayah.id == '1-1'