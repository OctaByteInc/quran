import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.utils.proto_converter import ProtoConverter
from quran.domain.image import Image
from quran.factory.image_factory import ImageFactory


class ImageService(image_rpc.ImageServicer):

    def CreateImage(self, request, context):
        image = Image.from_dict(ProtoConverter.proto_to_dict(request))
        create_image = ImageFactory.create()
        res = create_image.exec(image)
        return entity_proto.ImageEntity(**res.to_dict())

    def FindImageByAyahId(self, request, context):
        find_image = ImageFactory.find_image()
        image = find_image.by_ayah_id(request.id)
        return entity_proto.ImageEntity(**image.to_dict())
