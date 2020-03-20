# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import quran.endpoints.grpc.ayah_pb2 as ayah__pb2
import quran.endpoints.grpc.entity_pb2 as entity__pb2


class AyahStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateAyah = channel.unary_unary(
        '/quran.Ayah/CreateAyah',
        request_serializer=entity__pb2.AyahEntity.SerializeToString,
        response_deserializer=ayah__pb2.AyahEntityResponse.FromString,
        )
    self.FindAyahById = channel.unary_unary(
        '/quran.Ayah/FindAyahById',
        request_serializer=ayah__pb2.AyahIdRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahSingleResponse.FromString,
        )
    self.FindAyahBySurahId = channel.unary_unary(
        '/quran.Ayah/FindAyahBySurahId',
        request_serializer=ayah__pb2.AyahIdRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )
    self.FindAyahByNumber = channel.unary_unary(
        '/quran.Ayah/FindAyahByNumber',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahSingleResponse.FromString,
        )
    self.FindAyahByNumberInSurah = channel.unary_unary(
        '/quran.Ayah/FindAyahByNumberInSurah',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahSingleResponse.FromString,
        )
    self.FindAyahByJuz = channel.unary_unary(
        '/quran.Ayah/FindAyahByJuz',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )
    self.FindAyahByManzil = channel.unary_unary(
        '/quran.Ayah/FindAyahByManzil',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )
    self.FindAyahByRuku = channel.unary_unary(
        '/quran.Ayah/FindAyahByRuku',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )
    self.FindAyahByHizbQuarter = channel.unary_unary(
        '/quran.Ayah/FindAyahByHizbQuarter',
        request_serializer=ayah__pb2.AyahNumberRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )
    self.FindAyahBySajda = channel.unary_unary(
        '/quran.Ayah/FindAyahBySajda',
        request_serializer=ayah__pb2.AyahSajdaRequest.SerializeToString,
        response_deserializer=ayah__pb2.AyahMultiResponse.FromString,
        )


class AyahServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateAyah(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahBySurahId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByNumber(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByNumberInSurah(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByJuz(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByManzil(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByRuku(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahByHizbQuarter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAyahBySajda(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AyahServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateAyah': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAyah,
          request_deserializer=entity__pb2.AyahEntity.FromString,
          response_serializer=ayah__pb2.AyahEntityResponse.SerializeToString,
      ),
      'FindAyahById': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahById,
          request_deserializer=ayah__pb2.AyahIdRequest.FromString,
          response_serializer=ayah__pb2.AyahSingleResponse.SerializeToString,
      ),
      'FindAyahBySurahId': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahBySurahId,
          request_deserializer=ayah__pb2.AyahIdRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
      'FindAyahByNumber': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByNumber,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahSingleResponse.SerializeToString,
      ),
      'FindAyahByNumberInSurah': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByNumberInSurah,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahSingleResponse.SerializeToString,
      ),
      'FindAyahByJuz': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByJuz,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
      'FindAyahByManzil': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByManzil,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
      'FindAyahByRuku': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByRuku,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
      'FindAyahByHizbQuarter': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahByHizbQuarter,
          request_deserializer=ayah__pb2.AyahNumberRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
      'FindAyahBySajda': grpc.unary_unary_rpc_method_handler(
          servicer.FindAyahBySajda,
          request_deserializer=ayah__pb2.AyahSajdaRequest.FromString,
          response_serializer=ayah__pb2.AyahMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'quran.Ayah', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
