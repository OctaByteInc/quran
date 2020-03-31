import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.ayah_pb2 as ayah_proto
from quran.utils.proto_converter import ProtoConverter

channel = grpc.insecure_channel("localhost:50051")
stub = ayah_rpc.AyahStub(channel)


def test_create_ayah():
    ayah = entity_proto.AyahEntity(id='ayah-1', surah_id='surah-1', number=1, number_in_surah=1, juz=1, manzil=1,
                                   ruku=1, hizb_quarter=1, sajda=False, arabic='Arabic content for ayah 1')
    res = stub.CreateAyah(ayah)

    assert ProtoConverter.proto_to_dict(res.data.ayah_response) == ProtoConverter.proto_to_dict(ayah)


def test_find_ayah_by_id_without_parts():
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1'))

    assert response.data.ayah_response.ayah.id == 'ayah-1'
    assert response.data.ayah_response.ayah.number == 1


def test_find_ayah_by_id_with_parts():
    ayah_parts = ayah_proto.PartsRequest(edition_id='edition-1',
                                         list='Translation,Surah,Edition,Arabic_Audio,Translation_Audio,Image')
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1', parts=ayah_parts))

    assert response.data.ayah_response.ayah.id == 'ayah-1'
    assert response.data.ayah_response.translation.id == 'translation-1'
    assert response.data.ayah_response.surah.id == 'surah-1'
    assert response.data.ayah_response.edition.id == 'edition-1'
    assert response.data.ayah_response.arabic_audio.id == 'audio-1'
    assert response.data.ayah_response.arabic_audio.type == 'Arabic'
    assert response.data.ayah_response.translation_audio.id == 'audio-2'
    assert response.data.ayah_response.translation_audio.type == 'Translation'
    assert response.data.ayah_response.image.image == 'link to image'


def test_find_ayah_by_surah_id_without_parts():
    response_stream = stub.FindAyahBySurahId(ayah_proto.AyahIdRequest(id='surah-1'))

    for response in response_stream.data.ayah_response:
        assert response.ayah.surah_id == 'surah-1'


def test_find_ayah_by_surah_id_with_parts():
    ayah_parts = ayah_proto.PartsRequest(edition_id='edition-1',
                                         list='Translation,Surah,Edition,Arabic_Audio,Translation_Audio,Image')
    response_stream = stub.FindAyahBySurahId(ayah_proto.AyahIdRequest(id='surah-1', parts=ayah_parts))

    for response in response_stream.data.ayah_response:
        assert response.ayah.id == 'ayah-1'
        assert response.translation.id == 'translation-1'
        assert response.surah.id == 'surah-1'
        assert response.edition.id == 'edition-1'
        assert response.arabic_audio.id == 'audio-1'
        assert response.arabic_audio.type == 'Arabic'
        assert response.translation_audio.id == 'audio-2'
        assert response.translation_audio.type == 'Translation'
        assert response.image.image == 'link to image'
        break


def test_find_ayah_by_number():
    response = stub.FindAyahByNumber(ayah_proto.AyahNumberRequest(number=1))

    assert response.data.ayah_response.ayah.number == 1


def test_find_ayah_by_number_in_surah():
    response = stub.FindAyahByNumberInSurah(ayah_proto.AyahNumberRequest(number=1))

    assert response.data.ayah_response.ayah.number_in_surah == 1


def test_find_ayah_by_juz():
    response_stream = stub.FindAyahByJuz(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.data.ayah_response:
        assert response.ayah.juz == 1


def test_find_ayah_by_manzil():
    response_stream = stub.FindAyahByManzil(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.data.ayah_response:
        assert response.ayah.manzil == 1


def test_find_ayah_by_ruku():
    response_stream = stub.FindAyahByRuku(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.data.ayah_response:
        assert response.ayah.ruku == 1


def test_find_ayah_by_hizb_quarter():
    response_stream = stub.FindAyahByHizbQuarter(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.data.ayah_response:
        assert response.ayah.hizb_quarter == 1


def test_find_ayah_by_sajda():
    response_stream = stub.FindAyahBySajda(ayah_proto.AyahSajdaRequest(sajda=False))

    for response in response_stream.data.ayah_response:
        assert response.ayah.sajda == False


def test_find_ayah_by_juz_with_limit_and_cursor():
    # Create some dummy data
    ayah = entity_proto.AyahEntity(id='ayah-2', surah_id='surah-1', number=1, number_in_surah=1, juz=1, manzil=1,
                                   ruku=1, hizb_quarter=1, sajda=False, arabic='Arabic content for ayah 2')
    res = stub.CreateAyah(ayah)
    ayah = entity_proto.AyahEntity(id='ayah-3', surah_id='surah-1', number=1, number_in_surah=1, juz=1, manzil=1,
                                   ruku=1, hizb_quarter=1, sajda=False, arabic='Arabic content for ayah 3')
    res = stub.CreateAyah(ayah)
    ayah = entity_proto.AyahEntity(id='ayah-4', surah_id='surah-1', number=1, number_in_surah=1, juz=1, manzil=1,
                                   ruku=1, hizb_quarter=1, sajda=False, arabic='Arabic content for ayah 4')
    res = stub.CreateAyah(ayah)
    # End creation data

    response_stream = stub.FindAyahByJuz(ayah_proto.AyahNumberRequest(number=1, limit=2))

    cursor = response_stream.data.cursor
    assert cursor is not None

    count = 0
    for response in response_stream.data.ayah_response:
        assert response.ayah.juz == 1
        count += 1

    assert count == 2

    response_stream = stub.FindAyahByJuz(ayah_proto.AyahNumberRequest(cursor=cursor))

    count = 0
    for response in response_stream.data.ayah_response:
        assert response.ayah.juz == 1
        count += 1

    assert count == 2