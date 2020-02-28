from concurrent import futures
import time

import grpc

import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
import quran.endpoints.grpc.audio_pb2 as audio_proto
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.image import Image
from quran.domain.audio import Audio
from tests.quran.factory.audio_factory import AudioFactory
from tests.quran.factory.image_factory import ImageFactory
from quran.utils.proto_converter import ProtoConverter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class AudioService(audio_rpc.AudioServicer):

    def FindAudioByEditionId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio1 = entity_proto.AudioEntity(id='id', ayah_id='ayah-id', edition_id='edition-id', type='AUDIO_TRANSLATION',
                                          audio='audio')
        audio2 = entity_proto.AudioEntity(id='id', ayah_id='ayah-id', edition_id='edition-id', type='AUDIO_TRANSLATION',
                                          audio='audio')
        return audio_proto.AudioList(audio_entity=[audio1, audio2])

    def FindArabicAudio(self, request, context):
        dict_list = {}
        for r in request.filter:
            dict_list[r.name] = r.value
        print(dict_list)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio_rpc.add_AudioServicer_to_server(AudioService(), server)
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
