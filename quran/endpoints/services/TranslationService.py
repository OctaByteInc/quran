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
        return entity_proto.TranslationEntity(**res.to_dict())

    def FindTranslationById(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation = find_translation.by_id(request.id)
        return entity_proto.TranslationEntity(**translation.to_dict())

    def FindTranslationByAyahId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_ayah_id(request.id)
        translations = []
        for translation in translation_stream:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        return translation_proto.TranslationList(translation_entity=translations)

    def FindTranslationByEditionId(self, request, context):
        find_translation = TranslationFactory.find_translation()
        translation_stream = find_translation.by_edition_id(request.id)
        translations = []
        for translation in translation_stream:
            translations.append(entity_proto.TranslationEntity(**translation.to_dict()))

        return translation_proto.TranslationList(translation_entity=translations)

    def FilterTranslation(self, request, context):
        filters = {}
        for filter in request.filter:
            filters[filter.name] = filter.value

        find_translation = TranslationFactory.find_translation()
        translation = find_translation.filter(**filters)
        return entity_proto.TranslationEntity(**translation.to_dict())