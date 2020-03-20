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
        return entity_proto.SurahEntity(**res.to_dict())

    def GetAll(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah_stream = find_surah.get_all()
        surah_list = []
        for surah in surah_stream:
            surah_list.append(entity_proto.SurahEntity(**surah.to_dict()))

        return surah_proto.SurahList(surah_list=surah_list)

    def FindSurahById(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah = find_surah.by_id(request.id)
        return entity_proto.SurahEntity(**surah.to_dict())

    def FindSurahByNumber(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah = find_surah.by_number(request.number)
        return entity_proto.SurahEntity(**surah.to_dict())

    def FindSurahByName(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah = find_surah.by_name(request.name)
        return entity_proto.SurahEntity(**surah.to_dict())

    def FindSurahByEnglishName(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah = find_surah.by_english_name(request.name)
        return entity_proto.SurahEntity(**surah.to_dict())

    def FindSurahByRevelationType(self, request, context):
        find_surah = SurahFactory.find_surah()
        surah_stream = find_surah.by_revelation_type(request.revelation_type)
        surah_list = []
        for surah in surah_stream:
            surah_list.append(entity_proto.SurahEntity(**surah.to_dict()))

        return surah_proto.SurahList(surah_list=surah_list)