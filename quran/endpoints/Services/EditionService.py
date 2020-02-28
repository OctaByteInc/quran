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

        return entity_proto.EditionEntity(**res.to_dict())