import quran.endpoints.grpc.edition_pb2 as edition_proto
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.edition import Edition
from quran.factory.edition_factory import EditionFactory
from quran.utils.proto_converter import ProtoConverter


class EditionService(edition_rpc.EditionSvcServicer):

    def CreateEdition(self, request, context):
        edition = Edition.from_dict(ProtoConverter.proto_to_dict(request))
        create_edition = EditionFactory.create()
        res = create_edition.exec(edition)

        return entity_proto.Edition(**res.to_dict())

    def GetAll(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.get_all()
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)

    def FindEditionById(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition = find_edition.by_id(request.id)
        return entity_proto.Edition(**edition.to_dict())

    def FindEditionByLanguage(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_language(request.name)
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)

    def FindEditionByName(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_name(request.name)
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)

    def FindEditionByEnglishName(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_english_name(request.name)
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)

    def FindEditionByFormat(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_format(request.name)
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)

    def FindEditionByType(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_type(request.name)
        editions = []
        for edition in edition_stream:
            editions.append(entity_proto.Edition(**edition.to_dict()))

        return edition_proto.EditionList(edition_list=editions)