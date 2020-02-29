from concurrent import futures
import time

import grpc

import quran.endpoints.grpc.ayah_pb2 as ayah_proto
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.edition_pb2 as edition_proto
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
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


class AyahService(ayah_rpc.AyahServicer):

    def FindAyahById(self, request, context):
        ayah_entity1 = entity_proto.AyahEntity(id='12', surah_id='as', number=1, number_in_surah=2, juz=1, manzil=3,
                                              ruku=4, hizb_quarter=4, sajda=False)
        ayah_entity1.arabic = 'arabic-aksldn'
        return ayah_proto.AyahResponse(ayah_entity=ayah_entity1)


# class EditionService(edition_rpc.EditionServicer):
#
#     def GetAll(self, request, context):
#         print(request)
#         edition = entity_proto.EditionEntity(id='id', language='as', name='as', english_name='as', type='AUDIO_TRANSLATION',
#                                           format='s', direction='as')
#         return edition_proto.EditionList(edition_entity=[edition])
#
#     def FindById(self, request, context):
#         print(request)
#         return entity_proto.EditionEntity(id='id', language='as', name='as', english_name='as',
#                                           type='AUDIO_TRANSLATION',
#                                           format='s', direction='as')

class AudioService(audio_rpc.AudioServicer):

    def CreateAudio(self, request, context):
        audio = Audio.from_dict(ProtoConverter.proto_to_dict(request))
        print(audio)
        create_audio = AudioFactory.create_audio()
        res = create_audio.exec(audio)
        return entity_proto.AudioEntity(**res.to_dict())


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
    #ayah_rpc.add_AyahServicer_to_server(AyahService(), server)
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
