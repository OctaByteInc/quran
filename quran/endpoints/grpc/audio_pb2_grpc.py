# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import quran.endpoints.grpc.audio_pb2 as audio__pb2
import quran.endpoints.grpc.entity_pb2 as entity__pb2
import quran.endpoints.grpc.shared_pb2 as shared__pb2


class AudioStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateAudio = channel.unary_unary(
        '/quran.Audio/CreateAudio',
        request_serializer=entity__pb2.AudioEntity.SerializeToString,
        response_deserializer=entity__pb2.AudioEntity.FromString,
        )
    self.FindAudioById = channel.unary_unary(
        '/quran.Audio/FindAudioById',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=entity__pb2.AudioEntity.FromString,
        )
    self.FindAudioByAyahId = channel.unary_unary(
        '/quran.Audio/FindAudioByAyahId',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=entity__pb2.AudioEntity.FromString,
        )
    self.FindAudioByEditionId = channel.unary_unary(
        '/quran.Audio/FindAudioByEditionId',
        request_serializer=shared__pb2.IDRequest.SerializeToString,
        response_deserializer=audio__pb2.AudioList.FromString,
        )
    self.FindArabicAudio = channel.unary_unary(
        '/quran.Audio/FindArabicAudio',
        request_serializer=shared__pb2.FilterRequest.SerializeToString,
        response_deserializer=entity__pb2.AudioEntity.FromString,
        )
    self.FindTranslationAudio = channel.unary_unary(
        '/quran.Audio/FindTranslationAudio',
        request_serializer=shared__pb2.FilterRequest.SerializeToString,
        response_deserializer=entity__pb2.AudioEntity.FromString,
        )


class AudioServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateAudio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAudioById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAudioByAyahId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAudioByEditionId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindArabicAudio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindTranslationAudio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AudioServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateAudio': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAudio,
          request_deserializer=entity__pb2.AudioEntity.FromString,
          response_serializer=entity__pb2.AudioEntity.SerializeToString,
      ),
      'FindAudioById': grpc.unary_unary_rpc_method_handler(
          servicer.FindAudioById,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=entity__pb2.AudioEntity.SerializeToString,
      ),
      'FindAudioByAyahId': grpc.unary_unary_rpc_method_handler(
          servicer.FindAudioByAyahId,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=entity__pb2.AudioEntity.SerializeToString,
      ),
      'FindAudioByEditionId': grpc.unary_unary_rpc_method_handler(
          servicer.FindAudioByEditionId,
          request_deserializer=shared__pb2.IDRequest.FromString,
          response_serializer=audio__pb2.AudioList.SerializeToString,
      ),
      'FindArabicAudio': grpc.unary_unary_rpc_method_handler(
          servicer.FindArabicAudio,
          request_deserializer=shared__pb2.FilterRequest.FromString,
          response_serializer=entity__pb2.AudioEntity.SerializeToString,
      ),
      'FindTranslationAudio': grpc.unary_unary_rpc_method_handler(
          servicer.FindTranslationAudio,
          request_deserializer=shared__pb2.FilterRequest.FromString,
          response_serializer=entity__pb2.AudioEntity.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'quran.Audio', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
