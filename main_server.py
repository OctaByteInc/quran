from concurrent import futures
import time

import grpc

import quran.endpoints.grpc.image_pb2 as image_pb2
import quran.endpoints.grpc.image_pb2_grpc as image_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ImageService(image_pb2_grpc.ImageServicer):

    def CreateImage(self, request, context):
        return image_pb2.ImageEntity(ayah_id=request.ayah_id, image=request.image)

    def FindImageByAyahId(self, request, context):
        print(request)
        print(request.id)
        return image_pb2.ImageEntity(ayah_id='ayah_id', image='image')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServicer_to_server(ImageService(), server)
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
    serve()