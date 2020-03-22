import quran.endpoints.grpc.audio_pb2 as audio_proto
import quran.endpoints.grpc.audio_pb2_grpc as audio_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.audio import Audio
from quran.factory.audio_factory import AudioFactory
from quran.utils.proto_converter import ProtoConverter


class AudioService(audio_rpc.AudioServicer):

    def CreateAudio(self, request, context):
        audio = Audio.from_dict(ProtoConverter.proto_to_dict(request))
        create_audio = AudioFactory.create()
        res = create_audio.exec(audio)
        audio_entity = entity_proto.AudioEntity(**res.to_dict())
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_entity)

    def FindAudioById(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.by_id(request.id)

        if not audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**audio.to_dict())
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_entity)

    def FindAudioByAyahId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio_list = []
        audio_stream = find_audio.by_ayah_id(request.id)
        for audio in audio_stream:
            audio_list.append(entity_proto.AudioEntity(**audio.to_dict()))

        if len(audio_list) == 0:
            return audio_proto.AudioMultiResponse(code=404, status='Not Found')

        return audio_proto.AudioMultiResponse(code=200, status='OK', data=audio_list)

    def FindAudioByEditionId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio_list = []
        audio_stream = find_audio.by_edition_id(request.id)
        for audio in audio_stream:
            audio_list.append(entity_proto.AudioEntity(**audio.to_dict()))

        if len(audio_list) == 0:
            return audio_proto.AudioMultiResponse(code=404, status='Not Found')

        return audio_proto.AudioMultiResponse(code=200, status='OK', data=audio_list)

    def FindArabicAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.arabic_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)
        if not audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**audio.to_dict())
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_entity)

    def FindTranslationAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.translation_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)

        if not audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**audio.to_dict())
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_entity)
