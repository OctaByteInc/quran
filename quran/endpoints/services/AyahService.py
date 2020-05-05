import quran.endpoints.grpc.ayah_pb2 as ayah_proto
import quran.endpoints.grpc.ayah_pb2_grpc as ayah_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.ayah import Ayah
from quran.factory.ayah_factory import AyahFactory
from quran.utils.proto_converter import ProtoConverter

default_edition_id = 'edition-1'

class AyahService(ayah_rpc.AyahServicer):

    def CreateAyah(self, request, context):
        ayah = Ayah.from_dict(ProtoConverter.proto_to_dict(request))
        create_ayah = AyahFactory.create()
        res = create_ayah.exec(ayah)
        ayah_entity = entity_proto.AyahEntity(**res.ayah.to_dict())
        ayah_data = ayah_proto.AyahEntityData(ayah_response=ayah_entity, number_of_results=res.number_of_results)

        return ayah_proto.AyahEntityResponse(code=200, status='OK', data=ayah_data)

    def FindAyahById(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response = find_ayah.by_id(request.id, edition_id, ayah_parts)

        if response is None:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response.ayah)
        ayah_data = ayah_proto.AyahSingleData(ayah_response=ayah_response, number_of_results=response.number_of_results)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_data)

    def FindAyahBySurahId(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_surah_id(request.id, edition_id, ayah_parts, request.limit, request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByNumber(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response = find_ayah.by_number(request.number, edition_id, ayah_parts)
        if response is None:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response.ayah)
        ayah_data = ayah_proto.AyahSingleData(ayah_response=ayah_response, number_of_results=response.number_of_results)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByNumberInSurah(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response = find_ayah.by_number_in_surah(request.number, edition_id, ayah_parts)
        if response is None:
            return ayah_proto.AyahSingleResponse(code=404, status='Not Found')

        ayah_response = self._ayah_response(response.ayah)
        ayah_data = ayah_proto.AyahSingleData(ayah_response=ayah_response, number_of_results=response.number_of_results)
        return ayah_proto.AyahSingleResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByJuz(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_juz(request.number, edition_id, ayah_parts, request.limit, request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByManzil(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_manzil(request.number, edition_id, ayah_parts, request.limit, request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByRuku(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_ruku(request.number, edition_id, ayah_parts, request.limit, request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

    def FindAyahByHizbQuarter(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_hizb_quarter(request.number, edition_id, ayah_parts, request.limit,
                                                    request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

    def FindAyahBySajda(self, request, context):
        find_ayah = AyahFactory.find_ayah()
        edition_id = default_edition_id
        if request.parts.edition_id:
            edition_id = request.parts.edition_id
        ayah_parts = [part.title().strip() for part in request.parts.list.split(',')]
        response_stream = find_ayah.by_sajda(request.sajda, edition_id, ayah_parts, request.limit, request.cursor)
        response_list = []
        for response in response_stream.ayah_list:
            response_list.append(self._ayah_response(response))

        if len(response_list) == 0:
            return ayah_proto.AyahMultiResponse(code=404, status='Not Found')

        ayah_data = ayah_proto.AyahMultiData(ayah_response=response_list,
                                             number_of_results=response_stream.number_of_results,
                                             cursor=response_stream.cursor)
        return ayah_proto.AyahMultiResponse(code=200, status='OK', data=ayah_data)

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
