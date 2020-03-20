import quran.endpoints.grpc.translation_pb2 as translation_proto
import quran.endpoints.grpc.translation_pb2_grpc as translation_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.translation import Translation
from quran.factory.translation_factory import TranslationFactory
from quran.utils.proto_converter import ProtoConverter


class TranslationService(translation_rpc.TranslationServicer):

    def CreateTranslation(self, request, context):
        translation = Translation.from_dict(ProtoConverter.proto_to_dict(request))
        create_translation = TranslationFactory.create()
        res = create_translation.exec(translation)
        trans_entity = entity_proto.TranslationEntity(**res.to_dict())
        return translation_proto.TranslationSingleResponse(code=200, status='OK', data=trans_entity)

    def FindTranslationById(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation = find_translation.by_id(request.id)

        if not translation:
            return translation_proto.TranslationSingleResponse(code=404, status='Not Found')

        trans_entity = entity_proto.TranslationEntity(**translation.to_dict())
        return translation_proto.TranslationSingleResponse(code=200, status='OK', data=trans_entity)

    def FindTranslationByAyahId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_ayah_id(request.id)
        translations = []
        for translation in translation_stream:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        if len(translations) == 0:
            return translation_proto.TranslationMultiResponse(code=200, status='Not Found')

        return translation_proto.TranslationMultiResponse(code=200, status='OK', data=translations)

    def FindTranslationByEditionId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_edition_id(request.id)
        translations = []
        for translation in translation_stream:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        if len(translations) == 0:
            return translation_proto.TranslationMultiResponse(code=200, status='Not Found')

        return translation_proto.TranslationMultiResponse(code=200, status='OK', data=translations)

    def FilterTranslation(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation = find_translation.filter(ayah_id=request.ayah_id, edition_id=request.edition_id)
        return entity_proto.TranslationEntity(**translation.to_dict())