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
        audio_entity = entity_proto.AudioEntity(**res.audio.to_dict())
        audio_data = audio_proto.AudioSingleData(audio=audio_entity, number_of_results=1)
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_data)

    def FindAudioById(self, request, context):
        find_audio = AudioFactory.find_audio()
        res = find_audio.by_id(request.id)

        if not res.audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**res.audio.to_dict())
        audio_data = audio_proto.AudioSingleData(audio=audio_entity, number_of_results=res.number_of_results)
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_data)

    def FindAudioByAyahId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio_entities = []
        res = find_audio.by_ayah_id(request.id, request.limit, request.cursor)
        for audio in res.audio_list:
            audio_entities.append(entity_proto.AudioEntity(**audio.to_dict()))

        if len(audio_entities) == 0:
            return audio_proto.AudioMultiResponse(code=404, status='Not Found')

        audio_data = audio_proto.AudioMultiData(audio=audio_entities, number_of_results=res.number_of_results,
                                                cursor=res.cursor)
        return audio_proto.AudioMultiResponse(code=200, status='OK', data=audio_data)

    def FindAudioByEditionId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio_entities = []
        res = find_audio.by_edition_id(request.id, request.limit, request.cursor)
        for audio in res.audio_list:
            audio_entities.append(entity_proto.AudioEntity(**audio.to_dict()))

        if len(audio_entities) == 0:
            return audio_proto.AudioMultiResponse(code=404, status='Not Found')

        audio_data = audio_proto.AudioMultiData(audio=audio_entities, number_of_results=res.number_of_results,
                                                cursor=res.cursor)
        return audio_proto.AudioMultiResponse(code=200, status='OK', data=audio_data)

    def FindArabicAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        res = find_audio.arabic_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)
        if not res.audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**res.audio.to_dict())
        audio_data = audio_proto.AudioSingleData(audio=audio_entity, number_of_results=res.number_of_results)
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_data)

    def FindTranslationAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        res = find_audio.translation_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)

        if not res.audio:
            return audio_proto.AudioSingleResponse(code=404, status='Not Found')

        audio_entity = entity_proto.AudioEntity(**res.audio.to_dict())
        audio_data = audio_proto.AudioSingleData(audio=audio_entity, number_of_results=res.number_of_results)
        return audio_proto.AudioSingleResponse(code=200, status='OK', data=audio_data)
