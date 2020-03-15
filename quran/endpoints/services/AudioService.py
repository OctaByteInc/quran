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
        return entity_proto.AudioEntity(**res.to_dict())

    def FindAudioById(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.by_id(request.id)
        return entity_proto.AudioEntity(**audio.to_dict())

    def FindAudioByAyahId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.by_ayah_id(request.id)
        return entity_proto.AudioEntity(**audio.to_dict())

    def FindAudioByEditionId(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio_list = []
        audio_stream = find_audio.by_edition_id(request.id)
        for audio in audio_stream:
            audio_list.append(audio)

        return audio_proto.AudioList(audio_entity=audio_list)

    def FindArabicAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.arabic_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)
        return entity_proto.AudioEntity(**audio.to_dict())

    def FindTranslationAudio(self, request, context):
        find_audio = AudioFactory.find_audio()
        audio = find_audio.translation_audio(ayah_id=request.ayah_id, edition_id=request.edition_id)
        return entity_proto.AudioEntity(**audio.to_dict())