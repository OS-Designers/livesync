# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: remote_node/remote_node.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'remote_node/remote_node.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dremote_node/remote_node.proto\x12\x08livesync\x1a\x1cgoogle/protobuf/struct.proto\"=\n\x10\x43onfigureRequest\x12)\n\x08settings\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\";\n\x11\x43onfigureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"#\n\x0bStepRequest\x12\x14\n\x0ctarget_frame\x18\x01 \x01(\x0c\"h\n\x0cStepResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x0fprocessed_frame\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x12\x15\n\rerror_message\x18\x03 \x01(\tB\x12\n\x10_processed_frame2\x89\x01\n\nRemoteNode\x12\x44\n\tConfigure\x12\x1a.livesync.ConfigureRequest\x1a\x1b.livesync.ConfigureResponse\x12\x35\n\x04Step\x12\x15.livesync.StepRequest\x1a\x16.livesync.StepResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'remote_node.remote_node_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONFIGUREREQUEST']._serialized_start=73
  _globals['_CONFIGUREREQUEST']._serialized_end=134
  _globals['_CONFIGURERESPONSE']._serialized_start=136
  _globals['_CONFIGURERESPONSE']._serialized_end=195
  _globals['_STEPREQUEST']._serialized_start=197
  _globals['_STEPREQUEST']._serialized_end=232
  _globals['_STEPRESPONSE']._serialized_start=234
  _globals['_STEPRESPONSE']._serialized_end=338
  _globals['_REMOTENODE']._serialized_start=341
  _globals['_REMOTENODE']._serialized_end=478
# @@protoc_insertion_point(module_scope)
