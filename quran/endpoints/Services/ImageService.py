import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.domain.image import Image
from quran.factory.image_factory import ImageFactory


class ImageService(image_rpc.ImageServicer):

    def CreateImage(self, request, context):
        image = Image.from_dict(request)
        create_image = ImageFactory.create()
        res = create_image.exec(image)
        return entity_proto.ImageEntity(**res.to_dict())
