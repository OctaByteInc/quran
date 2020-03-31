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
        trans_entity = entity_proto.TranslationEntity(**res.translation.to_dict())
        trans_data = translation_proto.TranslationSingleData(translation=trans_entity,
                                                             number_of_results=res.number_of_results)
        return translation_proto.TranslationSingleResponse(code=200, status='OK', data=trans_data)

    def FindTranslationById(self, request, context):
        find_translation = TranslationFactory.find_translation()
        res = find_translation.by_id(request.id)

        if not res.translation:
            return translation_proto.TranslationSingleResponse(code=404, status='Not Found')

        trans_entity = entity_proto.TranslationEntity(**res.translation.to_dict())
        trans_data = translation_proto.TranslationSingleData(translation=trans_entity,
                                                             number_of_results=res.number_of_results)
        return translation_proto.TranslationSingleResponse(code=200, status='OK', data=trans_data)

    def FindTranslationByAyahId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_ayah_id(request.id, request.limit, request.cursor)
        translations = []
        for translation in translation_stream.translation_list:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        if len(translations) == 0:
            return translation_proto.TranslationMultiResponse(code=200, status='Not Found')

        trans_data = translation_proto.TranslationMultiData(translation=translations,
                                                            number_of_results=translation_stream.number_of_results,
                                                            cursor=translation_stream.cursor)
        return translation_proto.TranslationMultiResponse(code=200, status='OK', data=trans_data)

    def FindTranslationByEditionId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_edition_id(request.id, request.limit, request.cursor)
        translations = []
        for translation in translation_stream.translation_list:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        if len(translations) == 0:
            return translation_proto.TranslationMultiResponse(code=200, status='Not Found')

        trans_data = translation_proto.TranslationMultiData(translation=translations,
                                                            number_of_results=translation_stream.number_of_results,
                                                            cursor=translation_stream.cursor)
        return translation_proto.TranslationMultiResponse(code=200, status='OK', data=trans_data)

    def FilterTranslation(self, request, context):
        find_translation = TranslationFactory.find_translation()
        res = find_translation.filter(ayah_id=request.ayah_id, edition_id=request.edition_id)

        if not res.translation:
            return translation_proto.TranslationSingleResponse(code=404, status='Not Found')

        trans_entity = entity_proto.TranslationEntity(**res.translation.to_dict())
        trans_data = translation_proto.TranslationSingleData(translation=trans_entity,
                                                             number_of_results=res.number_of_results)
        return translation_proto.TranslationSingleResponse(code=200, status='OK', data=trans_data)
