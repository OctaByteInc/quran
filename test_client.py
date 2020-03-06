import argparse

import grpc

import quran.endpoints.grpc.ayah_pb2 as ayah_proto
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.edition_pb2 as edition_proto
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_proto


def run(host):
    channel = grpc.insecure_channel(host)
    stub = audio_rpc.AudioStub(channel)
    audio_entity = entity_proto.AudioEntity(id='id', ayah_id='ayah-id', edition_id='edition-id',
                                            type='AUDIO_TRANSLATION',
                                            audio='audio')
    response = stub.CreateAudio(audio_entity)
    print(response)
    # stub = ayah_rpc.AyahStub(channel)
    # response = stub.FindAyahById(shared_proto.IDRequest(id='id-123'))
    # print(response)
    # response = stub.FindById(shared_proto.EmptyMessage())
    # print(response)
    # stub = audio_rpc.AudioStub(channel)
    # filters = [
    #     shared_proto.StringFilter(name='ayah_id', value='ayah-id-123'),
    #     shared_proto.StringFilter(name='edition_id', value='edition-id-123')
    # ]
    # response = stub.FindArabicAudio(shared_proto.FilterRequest(filter=filters))
    # print(response)
    # for r in response.audio_entity:
    #     print(r.id, r.type)

def run2(host, api_key):
    channel = grpc.insecure_channel(host)
    metadata = []
    if api_key:
        metadata.append(('x-api-key', api_key))
    stub = audio_rpc.AudioStub(channel)
    response = stub.FindAudioById(shared_proto.IDRequest(id='id'), metadata=metadata)
    print(response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost:50051', help='The server host.')
    parser.add_argument(
        '--api_key', default=None, help='The API key to use for the call.')
    args = parser.parse_args()

    run2(args.host, args.api_key)
