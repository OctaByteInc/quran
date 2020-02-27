import argparse

import grpc

import quran.endpoints.grpc.image_pb2 as image_pb2
import quran.endpoints.grpc.image_pb2_grpc as image_pb2_grpc
import quran.endpoints.grpc.shared_pb2 as shared_pb2


def run(host):
    channel = grpc.insecure_channel(host)
    stub = image_pb2_grpc.ImageStub(channel)
    response = stub.CreateImage(image_pb2.ImageEntity(ayah_id='ayah-id-2', image='grpc-image-link2'))
    print(response.ayah_id, response.image)

def run2(host):
    channel = grpc.insecure_channel(host)
    stub = image_pb2_grpc.ImageStub(channel)
    response = stub.FindImageByAyahId(shared_pb2.AyahId(id="ayah-123"))
    print(response.ayah_id, response.image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--host', default='localhost:50051', help='The server host.')
    args = parser.parse_args()

    run2(args.host)
