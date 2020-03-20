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
        ayah_entity = entity_proto.AyahEntity(**res.to_dict())

        return ayah_proto.AyahEntityResponse(code=200, status='OK', data=ayah_entity)

    def FindAyahById(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_id(request.id, edition_id, ayah_parts)

        if not response.ayah:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_response)

    def FindAyahBySurahId(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_surah_id(request.id, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def FindAyahByNumber(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_number(request.number, edition_id, ayah_parts)
        if not response.ayah:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_response)

    def FindAyahByNumberInSurah(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response = find_ayah.by_number_in_surah(request.number, edition_id, ayah_parts)
        if not response.ayah:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_response)

    def FindAyahByJuz(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_juz(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def FindAyahByManzil(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_manzil(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def FindAyahByRuku(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_ruku(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def FindAyahByHizbQuarter(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_hizb_quarter(request.number, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def FindAyahBySajda(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = request.parts.edition_id
        ayah_parts = request.parts.list.split(',')
        response_stream = find_ayah.by_sajda(request.sajda, edition_id, ayah_parts)
        response_list = []
        for response in response_stream:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=response_list)

    def _ayah_response(self, response):
        ayah_response = ayah_proto.AyahResponse(ayah=entity_proto.AyahEntity(**response.ayah.to_dict()))

        if response.translation:
            ayah_response.translation.MergeFrom(entity_proto.TranslationEntity(**response.translation.to_dict()))
        if response.surah:
            ayah_response.surah.MergeFrom(entity_proto.SurahEntity(**response.surah.to_dict()))
        if response.edition:
            ayah_response.edition.MergeFrom(entity_proto.EditionEntity(**response.edition.to_dict()))
        if response.arabic_audio:
            ayah_response.arabic_audio.MergeFrom(entity_proto.AudioEntity(**response.arabic_audio.to_dict()))
        if response.translation_audio:
            ayah_response.translation_audio.MergeFrom(entity_proto.AudioEntity(**response.translation_audio.to_dict()))
        if response.ayah_image:
            ayah_response.image.MergeFrom(entity_proto.ImageEntity(**response.ayah_image.to_dict()))

        return ayah_response
