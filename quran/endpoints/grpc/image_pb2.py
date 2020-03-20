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
  serialized_pb=_b('\n\x0bimage.proto\x12\x05quran\x1a\x0cshared.proto\x1a\x0c\x65ntity.proto\"U\n\x13ImageSingleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\x12 \n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x12.quran.ImageEntity2\x8d\x01\n\x05Image\x12?\n\x0b\x43reateImage\x12\x12.quran.ImageEntity\x1a\x1a.quran.ImageSingleResponse\"\x00\x12\x43\n\x11\x46indImageByAyahId\x12\x10.quran.IDRequest\x1a\x1a.quran.ImageSingleResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,entity__pb2.DESCRIPTOR,])




_IMAGESINGLERESPONSE = _descriptor.Descriptor(
  name='ImageSingleResponse',
  full_name='quran.ImageSingleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='quran.ImageSingleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='quran.ImageSingleResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='quran.ImageSingleResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=135,
)

_IMAGESINGLERESPONSE.fields_by_name['data'].message_type = entity__pb2._IMAGEENTITY
DESCRIPTOR.message_types_by_name['ImageSingleResponse'] = _IMAGESINGLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageSingleResponse = _reflection.GeneratedProtocolMessageType('ImageSingleResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGESINGLERESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:quran.ImageSingleResponse)
  })
_sym_db.RegisterMessage(ImageSingleResponse)



_IMAGE = _descriptor.ServiceDescriptor(
  name='Image',
  full_name='quran.Image',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=138,
  serialized_end=279,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateImage',
    full_name='quran.Image.CreateImage',
    index=0,
    containing_service=None,
    input_type=entity__pb2._IMAGEENTITY,
    output_type=_IMAGESINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindImageByAyahId',
    full_name='quran.Image.FindImageByAyahId',
    index=1,
    containing_service=None,
    input_type=shared__pb2._IDREQUEST,
    output_type=_IMAGESINGLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGE)

DESCRIPTOR.services_by_name['Image'] = _IMAGE

# @@protoc_insertion_point(module_scope)
