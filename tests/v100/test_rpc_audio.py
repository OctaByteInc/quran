import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
from quran.utils.proto_converter import ProtoConverter

channel = grpc.insecure_channel("localhost:50051")
stub = audio_rpc.AudioStub(channel)


def test_create_audio():
    audio = entity_proto.AudioEntity(id='audio-1', ayah_id='ayah-1', edition_id='edition-1', type='Arabic',
                                     audio='audio link for arabic 1')
    res = stub.CreateAudio(audio)

    assert ProtoConverter.proto_to_dict(res) == ProtoConverter.proto_to_dict(audio)


def test_find_audio_by_id():
    res = stub.FindAudioById(shared_entity.IDRequest(id='audio-1'))

    assert res.id == 'audio-1'
    assert res.ayah_id == 'ayah-1'


def test_find_audio_by_ayah_id():
    res_stream = stub.FindAudioByAyahId(shared_entity.IDRequest(id='ayah-1'))

    for res in res_stream.audio_list:
        assert res.ayah_id == 'ayah-1'


def test_find_audio_by_edition_id():
    res_stream = stub.FindAudioByEditionId(shared_entity.IDRequest(id='edition-1'))

    for res in res_stream.audio_list:
        assert res.edition_id == 'edition-1'


def test_find_arabic_audio():
    res = stub.FindArabicAudio(shared_entity.FilterRequest(ayah_id='ayah-1', edition_id='edition-1'))

    assert res.ayah_id == 'ayah-1'
    assert res.edition_id == 'edition-1'
    assert res.type == 'Arabic'


def test_find_translation_audio():
    audio = entity_proto.AudioEntity(id='audio-2', ayah_id='ayah-1', edition_id='edition-1', type='Translation',
                                     audio='audio link for translation 1')
    stub.CreateAudio(audio)

    res = stub.FindTranslationAudio(shared_entity.FilterRequest(ayah_id='ayah-1', edition_id='edition-1'))

    assert res.ayah_id == 'ayah-1'
    assert res.edition_id == 'edition-1'
    assert res.type == 'Translation'
