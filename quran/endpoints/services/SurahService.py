import quran.endpoints.grpc.surah_pb2 as surah_proto
import quran.endpoints.grpc.surah_pb2_grpc as surah_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.surah import Surah
from quran.factory.surah_factory import SurahFactory
from quran.utils.proto_converter import ProtoConverter


class SurahService(surah_rpc.SurahServicer):

    def CreateSurah(self, request, context):
        surah = Surah.from_dict(ProtoConverter.proto_to_dict(request))
        create_surah = SurahFactory.create()
        res = create_surah.exec(surah)
        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=res.number_of_results)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def GetAll(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah_stream = find_surah.get_all(request.limit, request.cursor)
        surah_list = []
        for surah in surah_stream.surah_list:
            surah_list.append(entity_proto.SurahEntity(**surah.to_dict()))

        if len(surah_list) == 0:
            return surah_proto.SurahMultiResponse(code=404, status='Not Found')

        surah_data = surah_proto.SurahMultiData(surah=surah_list, number_of_results=surah_stream.number_of_results,
                                                cursor=surah_stream.cursor)
        return surah_proto.SurahMultiResponse(code=200, status='OK', data=surah_data)

    def FindSurahById(self, request, context):
        find_surah = SurahFactory.find_surah()
        res = find_surah.by_id(request.id)

        if res is None:
            return surah_proto.SurahSingleResponse(code=404, status='Not Found')

        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=res.number_of_results)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def FindSurahByNumber(self, request, context):
        find_surah = SurahFactory.find_surah()
        res = find_surah.by_number(request.number)

        if res is None:
            return surah_proto.SurahSingleResponse(code=404, status='Not Found')

        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=res.number_of_results)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def FindSurahByName(self, request, context):
        find_surah = SurahFactory.find_surah()
        res = find_surah.by_name(request.name)

        if res is None:
            return surah_proto.SurahSingleResponse(code=404, status='Not Found')

        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=res.number_of_results)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def FindSurahByEnglishName(self, request, context):
        find_surah = SurahFactory.find_surah()
        res = find_surah.by_english_name(request.name)

        if res is None:
            return surah_proto.SurahSingleResponse(code=404, status='Not Found')

        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=1)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def FindSurahByEnglishNameTranslation(self, request, context):
        find_surah = SurahFactory.find_surah()
        res = find_surah.by_english_name_translation(request.name)

        if res is None:
            return surah_proto.SurahSingleResponse(code=404, status='Not Found')

        surah_entity = entity_proto.SurahEntity(**res.surah.to_dict())
        surah_data = surah_proto.SurahSingleData(surah=surah_entity, number_of_results=1)
        return surah_proto.SurahSingleResponse(code=200, status='OK', data=surah_data)

    def FindSurahByRevelationType(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah_stream = find_surah.by_revelation_type(request.revelation_type, request.limit, request.cursor)
        surah_list = []
        for surah in surah_stream.surah_list:
            surah_list.append(entity_proto.SurahEntity(**surah.to_dict()))

        if len(surah_list) == 0:
            return surah_proto.SurahMultiResponse(code=404, status='Not Found')

        surah_data = surah_proto.SurahMultiData(surah=surah_list, number_of_results=surah_stream.number_of_results,
                                                cursor=surah_stream.cursor)
        return surah_proto.SurahMultiResponse(code=200, status='OK', data=surah_data)
