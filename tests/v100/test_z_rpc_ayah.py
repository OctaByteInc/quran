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

    assert ProtoConverter.proto_to_dict(res) == ProtoConverter.proto_to_dict(ayah)


def test_find_ayah_by_id_without_parts():
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1'))

    assert response.ayah_entity.id == 'ayah-1'
    assert response.ayah_entity.number == 1


def test_find_ayah_by_id_with_parts():
    ayah_parts = ayah_proto.PartsRequest(edition_id='edition-1',
                                         list='Translation,Surah,Edition,Arabic_Audio,Translation_Audio,Image')
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1', parts=ayah_parts))

    assert response.ayah_entity.id == 'ayah-1'
    assert response.translation_entity.id == 'translation-1'
    assert response.surah_entity.id == 'surah-1'
    assert response.edition_entity.id == 'edition-1'
    assert response.arabic_audio.id == 'audio-1'
    assert response.arabic_audio.type == 'Arabic'
    assert response.translation_audio.id == 'audio-2'
    assert response.translation_audio.type == 'Translation'
    assert response.image_entity.image == 'link to image'


def find_ayah_by_surah_id_without_parts():
    response_stream = stub.FindAyahBySurahId(ayah_proto.AyahIdRequest(id='surah-1'))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.surah_id == 'surah-1'


def find_ayah_by_surah_id_with_parts():
    ayah_parts = ayah_proto.PartsRequest(edition_id='edition-1',
                                         list='Translation,Surah,Edition,Arabic_Audio,Translation_Audio,Image')
    response_stream = stub.FindAyahBySurahId(ayah_proto.AyahIdRequest(id='surah-1', parts=ayah_parts))
    response = next(response_stream.ayah_response)

    assert response.ayah_entity.id == 'ayah-1'
    assert response.translation_entity.id == 'translation-1'
    assert response.surah_entity.id == 'surah-1'
    assert response.edition_entity.id == 'edition-1'
    assert response.arabic_audio.id == 'audio-1'
    assert response.arabic_audio.type == 'Arabic'
    assert response.translation_audio.id == 'audio-2'
    assert response.translation_audio.type == 'Translation'
    assert response.image_entity.image == 'link to image'


def find_ayah_by_number():
    response = stub.FindAyahById(ayah_proto.AyahNumberRequest(number=1))

    assert response.ayah_entity.number == 1


def find_ayah_by_number_in_surah():
    response = stub.FindAyahByNumberInSurah(ayah_proto.AyahNumberRequest(number=1))

    assert response.ayah_entity.number_in_surah == 1


def find_ayah_by_juz():
    response_stream = stub.FindAyahByJuz(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.juz == 1


def find_ayah_by_manzil():
    response_stream = stub.FindAyahByManzil(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.manzil == 1


def find_ayah_by_ruku():
    response_stream = stub.FindAyahByRuku(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.ruku == 1


def find_ayah_by_hizb_quarter():
    response_stream = stub.FindAyahByHizbQuarter(ayah_proto.AyahNumberRequest(number=1))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.hizb_quarter == 1


def find_ayah_by_sajda():
    response_stream = stub.FindAyahBySajda(ayah_proto.AyahSajdaRequest(sajda=False))

    for response in response_stream.ayah_response:
        assert response.ayah_entity.sajda == False
