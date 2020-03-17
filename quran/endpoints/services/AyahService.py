import quran.endpoints.grpc.ayah_pb2 as ayah_proto
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.ayah import Ayah
from quran.factory.ayah_factory import AyahFactory
from quran.utils.proto_converter import ProtoConverter


class AyahService(ayah_rpc.AyahServicer):

    def CreateAyah(self, request, context):
        ayah = Ayah.from_dict(ProtoConverter.proto_to_dict(request))
        create_ayah = AyahFactory.create()
        res = create_ayah.exec(ayah)
        return entity_proto.AyahEntity(**res.to_dict())

    def FindAyahById(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_id(request.id, edition_id, ayah_parts)
        return self._ayah_response(response)

    def FindAyahBySurahId(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_surah_id(request.id, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def FindAyahByNumber(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_number(request.number, edition_id, ayah_parts)
        return self._ayah_response(response)

    def FindAyahByNumberInSurah(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_number_in_surah(request.number, edition_id, ayah_parts)
        return self._ayah_response(response)

    def FindAyahByJuz(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_juz(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def FindAyahByManzil(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_manzil(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def FindAyahByRuku(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_ruku(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def FindAyahByHizbQuarter(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_hizb_quarter(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def FindAyahBySajda(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_sajda(request.sajda, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        return ayah_proto.AyahList(ayah_response=response_list)

    def _ayah_response(self, response):
        ayah_response = ayah_proto.AyahResponse(ayah_entity=entity_proto.AyahEntity(**response.ayah.to_dict()))

        if response.translation:
            ayah_response.translation_entity.MergeFrom(entity_proto.TranslationEntity(**response.translation.to_dict()))
        if response.surah:
            ayah_response.surah_entity.MergeFrom(entity_proto.SurahEntity(**response.surah.to_dict()))
        if response.edition:
            ayah_response.edition_entity.MergeFrom(entity_proto.EditionEntity(**response.edition.to_dict()))
        if response.arabic_audio:
            ayah_response.arabic_audio.MergeFrom(entity_proto.AudioEntity(**response.arabic_audio.to_dict()))
        if response.translation_audio:
            ayah_response.translation_audio.MergeFrom(entity_proto.AudioEntity(**response.translation_audio.to_dict()))
        if response.ayah_image:
            ayah_response.image_entity.MergeFrom(entity_proto.ImageEntity(**response.ayah_image.to_dict()))

        return ayah_response
