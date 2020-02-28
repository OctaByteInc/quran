from concurrent import futures
import time

import grpc

import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.image import Image
from tests.quran.factory.image_factory import ImageFactory
from quran.utils.proto_converter import ProtoConverter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ImageService(image_rpc.ImageServicer):

    def CreateImage(self, request, context):
        image = Image.from_dict(ProtoConverter.proto_to_dict(request))
        create_image = ImageFactory.create()
        res = create_image.exec(image)
        return entity_proto.ImageEntity(**res.to_dict())

    def FindImageByAyahId(self, request, context):
        return entity_proto.ImageEntity(ayah_id='ayah-1', image='image-1')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_rpc.add_ImageServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # gRPC starts a new thread to service requests. Just make the main thread
    # sleep.
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(grace=0)


if __name__ == '__main__':
    print("Server start...")
    serve()