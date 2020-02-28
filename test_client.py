import argparse

import grpc

import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto


def run(host):
    channel = grpc.insecure_channel(host)
    stub = image_rpc.ImageStub(channel)
    response = stub.CreateImage(entity_proto.ImageEntity(ayah_id='ayah-id-2', image='grpc-image-link2'))
    print(response.ayah_id, response.image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost:50051', help='The server host.')
    args = parser.parse_args()

    run(args.host)
