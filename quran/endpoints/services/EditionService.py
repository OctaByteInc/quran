import quran.endpoints.grpc.edition_pb2 as edition_proto
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.edition import Edition
from quran.factory.edition_factory import EditionFactory
from quran.utils.proto_converter import ProtoConverter


class EditionService(edition_rpc.EditionServicer):

    def CreateEdition(self, request, context):
        edition = Edition.from_dict(ProtoConverter.proto_to_dict(request))
        create_edition = EditionFactory.create()
        res = create_edition.exec(edition)

        edition_entity = entity_proto.EditionEntity(**res.edition.to_dict())
        edition_data = edition_proto.EditionSingleData(edition=edition_entity, number_of_results=res.number_of_results)
        return edition_proto.EditionSingleResponse(code=200, status='OK', data=edition_data)

    def GetAll(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.get_all(request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)

    def FindEditionById(self, request, context):
        find_edition = EditionFactory.find_edition()
        res = find_edition.by_id(request.id)

        if res is None:
            return edition_proto.EditionSingleResponse(code=404, status='Not Found')

        edition_entity = entity_proto.EditionEntity(**res.edition.to_dict())
        edition_data = edition_proto.EditionSingleData(edition=edition_entity, number_of_results=res.number_of_results)
        return edition_proto.EditionSingleResponse(code=200, status='OK', data=edition_data)

    def FindEditionByLanguage(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_language(request.name, request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)

    def FindEditionByName(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_name(request.name, request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)

    def FindEditionByTranslator(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_translator(request.name, request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)

    def FindEditionByFormat(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_format(request.name, request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)

    def FindEditionByType(self, request, context):
        find_edition = EditionFactory.find_edition()
        edition_stream = find_edition.by_type(request.name, request.limit, request.cursor)
        editions = []
        for edition in edition_stream.edition_list:
            editions.append(entity_proto.EditionEntity(**edition.to_dict()))

        if len(editions) == 0:
            return edition_proto.EditionMultiResponse(code=404, status='Not Found')

        edition_data = edition_proto.EditionMultiData(edition=editions,
                                                      number_of_results=edition_stream.number_of_results,
                                                      cursor=edition_stream.cursor)
        return edition_proto.EditionMultiResponse(code=200, status='OK', data=edition_data)
