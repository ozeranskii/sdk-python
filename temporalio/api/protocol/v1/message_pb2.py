# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/protocol/v1/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&temporal/api/protocol/v1/message.proto\x12\x18temporal.api.protocol.v1\x1a\x19google/protobuf/any.proto"\x95\x01\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1c\n\x14protocol_instance_id\x18\x02 \x01(\t\x12\x12\n\x08\x65vent_id\x18\x03 \x01(\x03H\x00\x12\x17\n\rcommand_index\x18\x04 \x01(\x03H\x00\x12"\n\x04\x62ody\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyB\x0f\n\rsequencing_idB\x93\x01\n\x1bio.temporal.api.protocol.v1B\x0cMessageProtoP\x01Z\'go.temporal.io/api/protocol/v1;protocol\xaa\x02\x1aTemporalio.Api.Protocol.V1\xea\x02\x1dTemporalio::Api::Protocol::V1b\x06proto3'
)


_MESSAGE = DESCRIPTOR.message_types_by_name["Message"]
Message = _reflection.GeneratedProtocolMessageType(
    "Message",
    (_message.Message,),
    {
        "DESCRIPTOR": _MESSAGE,
        "__module__": "temporal.api.protocol.v1.message_pb2"
        # @@protoc_insertion_point(class_scope:temporal.api.protocol.v1.Message)
    },
)
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\033io.temporal.api.protocol.v1B\014MessageProtoP\001Z'go.temporal.io/api/protocol/v1;protocol\252\002\032Temporalio.Api.Protocol.V1\352\002\035Temporalio::Api::Protocol::V1"
    _MESSAGE._serialized_start = 96
    _MESSAGE._serialized_end = 245
# @@protoc_insertion_point(module_scope)