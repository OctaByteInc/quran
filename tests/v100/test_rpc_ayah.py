import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.ayah_pb2 as ayah_proto
from quran.utils.proto_converter import ProtoConverter

channel = grpc.insecure_channel("localhost:50051")
stub = ayah_rpc.AyahStub(channel)


def create_ayah():
    ayah = entity_proto.AyahEntity(id='ayah-1', surah_id='surah-1', number=1, number_in_surah=1, juz=1, manzil=1,
                                   ruku=1, hizb_quarter=1, sajda=False, arabic='Arabic content for ayah 1')
    res = stub.CreateAyah(ayah)

    assert ProtoConverter.proto_to_dict(res) == ProtoConverter.proto_to_dict(ayah)


def find_ayah_by_id_without_parts():
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1'))

    assert response.ayah_entity.id == 'ayah-1'
    assert response.ayah_entity.number == 1
    assert response.translation_entity is None


def find_ayah_by_id_with_parts():
    ayah_parts = ayah_proto.PartsRequest(edition_id='edition-1', parts='Translation, Surah, Edition')
    response = stub.FindAyahById(ayah_proto.AyahIdRequest(id='ayah-1', parts=ayah_parts))