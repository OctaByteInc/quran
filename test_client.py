import argparse

import grpc

import quran.endpoints.grpc.edition_pb2 as edition_proto
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_proto


def run(host):
    channel = grpc.insecure_channel(host)
    stub = edition_rpc.EditionStub(channel)
    response = stub.GetAll(shared_proto.EmptyMessage())
    #response = stub.FindById(shared_proto.EmptyMessage())
    print(response)
    # stub = audio_rpc.AudioStub(channel)
    # filters = [
    #     shared_proto.StringFilter(name='ayah_id', value='ayah-id-123'),
    #     shared_proto.StringFilter(name='edition_id', value='edition-id-123')
    # ]
    # response = stub.FindArabicAudio(shared_proto.FilterRequest(filter=filters))
    # print(response)
    # for r in response.audio_entity:
    #     print(r.id, r.type)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost:50051', help='The server host.')
    args = parser.parse_args()

    run(args.host)
