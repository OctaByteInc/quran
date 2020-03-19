# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import quran.endpoints.grpc.shared_pb2 as shared__pb2
import quran.endpoints.grpc.entity_pb2 as entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='quran',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bimage.proto\x12\x05quran\x1a\x0cshared.proto\x1a\x0c\x65ntity.proto2n\n\x08ImageSvc\x12+\n\x0b\x43reateImage\x12\x0c.quran.Image\x1a\x0c.quran.Image\"\x00\x12\x35\n\x11\x46indImageByAyahId\x12\x10.quran.IDRequest\x1a\x0c.quran.Image\"\x00\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,entity__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_IMAGESVC = _descriptor.ServiceDescriptor(
  name='ImageSvc',
  full_name='quran.ImageSvc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=50,
  serialized_end=160,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateImage',
    full_name='quran.ImageSvc.CreateImage',
    index=0,
    containing_service=None,
    input_type=entity__pb2._IMAGE,
    output_type=entity__pb2._IMAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindImageByAyahId',
    full_name='quran.ImageSvc.FindImageByAyahId',
    index=1,
    containing_service=None,
    input_type=shared__pb2._IDREQUEST,
    output_type=entity__pb2._IMAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESVC)

DESCRIPTOR.services_by_name['ImageSvc'] = _IMAGESVC

# @@protoc_insertion_point(module_scope)
