from concurrent import futures
import time
import grpc

import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.surah_pb2_grpc as surah_rpc
import quran.endpoints.grpc.translation_pb2_grpc as translation_rpc

from quran.endpoints.services.AudioService import AudioService
from quran.endpoints.services.AyahService import AyahService
from quran.endpoints.services.EditionService import EditionService
from quran.endpoints.services.ImageService import ImageService
from quran.endpoints.services.SurahService import SurahService
from quran.endpoints.services.TranslationService import TranslationService


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    audio_rpc.add_AudioServicer_to_server(AudioService(), server)
    ayah_rpc.add_AyahServicer_to_server(AyahService(), server)
    edition_rpc.add_EditionServicer_to_server(EditionService(), server)
    image_rpc.add_ImageServicer_to_server(ImageService(), server)
    surah_rpc.add_SurahServicer_to_server(SurahService(), server)
    translation_rpc.add_TranslationServicer_to_server(TranslationService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(grace=0)


if __name__ == '__main__':
    serve()