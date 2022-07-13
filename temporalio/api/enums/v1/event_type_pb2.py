# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/enums/v1/event_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&temporal/api/enums/v1/event_type.proto\x12\x15temporal.api.enums.v1*\xd7\x0e\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12)\n%EVENT_TYPE_WORKFLOW_EXECUTION_STARTED\x10\x01\x12+\n\'EVENT_TYPE_WORKFLOW_EXECUTION_COMPLETED\x10\x02\x12(\n$EVENT_TYPE_WORKFLOW_EXECUTION_FAILED\x10\x03\x12+\n\'EVENT_TYPE_WORKFLOW_EXECUTION_TIMED_OUT\x10\x04\x12&\n"EVENT_TYPE_WORKFLOW_TASK_SCHEDULED\x10\x05\x12$\n EVENT_TYPE_WORKFLOW_TASK_STARTED\x10\x06\x12&\n"EVENT_TYPE_WORKFLOW_TASK_COMPLETED\x10\x07\x12&\n"EVENT_TYPE_WORKFLOW_TASK_TIMED_OUT\x10\x08\x12#\n\x1f\x45VENT_TYPE_WORKFLOW_TASK_FAILED\x10\t\x12&\n"EVENT_TYPE_ACTIVITY_TASK_SCHEDULED\x10\n\x12$\n EVENT_TYPE_ACTIVITY_TASK_STARTED\x10\x0b\x12&\n"EVENT_TYPE_ACTIVITY_TASK_COMPLETED\x10\x0c\x12#\n\x1f\x45VENT_TYPE_ACTIVITY_TASK_FAILED\x10\r\x12&\n"EVENT_TYPE_ACTIVITY_TASK_TIMED_OUT\x10\x0e\x12-\n)EVENT_TYPE_ACTIVITY_TASK_CANCEL_REQUESTED\x10\x0f\x12%\n!EVENT_TYPE_ACTIVITY_TASK_CANCELED\x10\x10\x12\x1c\n\x18\x45VENT_TYPE_TIMER_STARTED\x10\x11\x12\x1a\n\x16\x45VENT_TYPE_TIMER_FIRED\x10\x12\x12\x1d\n\x19\x45VENT_TYPE_TIMER_CANCELED\x10\x13\x12\x32\n.EVENT_TYPE_WORKFLOW_EXECUTION_CANCEL_REQUESTED\x10\x14\x12*\n&EVENT_TYPE_WORKFLOW_EXECUTION_CANCELED\x10\x15\x12\x43\n?EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED\x10\x16\x12@\n<EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED\x10\x17\x12;\n7EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_CANCEL_REQUESTED\x10\x18\x12\x1e\n\x1a\x45VENT_TYPE_MARKER_RECORDED\x10\x19\x12*\n&EVENT_TYPE_WORKFLOW_EXECUTION_SIGNALED\x10\x1a\x12,\n(EVENT_TYPE_WORKFLOW_EXECUTION_TERMINATED\x10\x1b\x12\x32\n.EVENT_TYPE_WORKFLOW_EXECUTION_CONTINUED_AS_NEW\x10\x1c\x12\x37\n3EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_INITIATED\x10\x1d\x12\x34\n0EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_FAILED\x10\x1e\x12/\n+EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_STARTED\x10\x1f\x12\x31\n-EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_COMPLETED\x10 \x12.\n*EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_FAILED\x10!\x12\x30\n,EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_CANCELED\x10"\x12\x31\n-EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TIMED_OUT\x10#\x12\x32\n.EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TERMINATED\x10$\x12;\n7EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED\x10%\x12\x38\n4EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED\x10&\x12\x33\n/EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_SIGNALED\x10\'\x12\x30\n,EVENT_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES\x10(B\x82\x01\n\x18io.temporal.api.enums.v1B\x0e\x45ventTypeProtoP\x01Z!go.temporal.io/api/enums/v1;enums\xaa\x02\x15Temporal.Api.Enums.V1\xea\x02\x18Temporal::Api::Enums::V1b\x06proto3'
)

_EVENTTYPE = DESCRIPTOR.enum_types_by_name["EventType"]
EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
EVENT_TYPE_UNSPECIFIED = 0
EVENT_TYPE_WORKFLOW_EXECUTION_STARTED = 1
EVENT_TYPE_WORKFLOW_EXECUTION_COMPLETED = 2
EVENT_TYPE_WORKFLOW_EXECUTION_FAILED = 3
EVENT_TYPE_WORKFLOW_EXECUTION_TIMED_OUT = 4
EVENT_TYPE_WORKFLOW_TASK_SCHEDULED = 5
EVENT_TYPE_WORKFLOW_TASK_STARTED = 6
EVENT_TYPE_WORKFLOW_TASK_COMPLETED = 7
EVENT_TYPE_WORKFLOW_TASK_TIMED_OUT = 8
EVENT_TYPE_WORKFLOW_TASK_FAILED = 9
EVENT_TYPE_ACTIVITY_TASK_SCHEDULED = 10
EVENT_TYPE_ACTIVITY_TASK_STARTED = 11
EVENT_TYPE_ACTIVITY_TASK_COMPLETED = 12
EVENT_TYPE_ACTIVITY_TASK_FAILED = 13
EVENT_TYPE_ACTIVITY_TASK_TIMED_OUT = 14
EVENT_TYPE_ACTIVITY_TASK_CANCEL_REQUESTED = 15
EVENT_TYPE_ACTIVITY_TASK_CANCELED = 16
EVENT_TYPE_TIMER_STARTED = 17
EVENT_TYPE_TIMER_FIRED = 18
EVENT_TYPE_TIMER_CANCELED = 19
EVENT_TYPE_WORKFLOW_EXECUTION_CANCEL_REQUESTED = 20
EVENT_TYPE_WORKFLOW_EXECUTION_CANCELED = 21
EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = 22
EVENT_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = 23
EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_CANCEL_REQUESTED = 24
EVENT_TYPE_MARKER_RECORDED = 25
EVENT_TYPE_WORKFLOW_EXECUTION_SIGNALED = 26
EVENT_TYPE_WORKFLOW_EXECUTION_TERMINATED = 27
EVENT_TYPE_WORKFLOW_EXECUTION_CONTINUED_AS_NEW = 28
EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_INITIATED = 29
EVENT_TYPE_START_CHILD_WORKFLOW_EXECUTION_FAILED = 30
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_STARTED = 31
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_COMPLETED = 32
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_FAILED = 33
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_CANCELED = 34
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TIMED_OUT = 35
EVENT_TYPE_CHILD_WORKFLOW_EXECUTION_TERMINATED = 36
EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED = 37
EVENT_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED = 38
EVENT_TYPE_EXTERNAL_WORKFLOW_EXECUTION_SIGNALED = 39
EVENT_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES = 40


if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030io.temporal.api.enums.v1B\016EventTypeProtoP\001Z!go.temporal.io/api/enums/v1;enums\252\002\025Temporal.Api.Enums.V1\352\002\030Temporal::Api::Enums::V1"
    _EVENTTYPE._serialized_start = 66
    _EVENTTYPE._serialized_end = 1945
# @@protoc_insertion_point(module_scope)