import quran.endpoints.grpc.image_pb2_grpc as image_rpc
import quran.endpoints.grpc.image_pb2 as image_proto
import quran.endpoints.grpc.entity_pb2 as entity_proto
from quran.utils.proto_converter import ProtoConverter
from quran.domain.image import Image
from quran.factory.image_factory import ImageFactory


class ImageService(image_rpc.ImageServicer):

    def CreateImage(self, request, context):
        image = Image.from_dict(ProtoConverter.proto_to_dict(request))
        create_image = ImageFactory.create()
        res = create_image.exec(image)
        image_entity = entity_proto.ImageEntity(**res.image.to_dict())
        image_data = image_proto.ImageSingleData(image=image_entity, number_of_results=res.number_of_results)
        return image_proto.ImageSingleResponse(code=200, status='Ok', data=image_data)

    def FindImageByAyahId(self, request, context):
        find_image = ImageFactory.find_image()
        res = find_image.by_ayah_id(request.id)

        if not res.image:
            return image_proto.ImageSingleResponse(code=404, status='Not Found')

        image_entity = entity_proto.ImageEntity(**res.image.to_dict())
        image_data = image_proto.ImageSingleData(image=image_entity, number_of_results=res.number_of_results)
        return image_proto.ImageSingleResponse(code=200, status='Ok', data=image_data)
