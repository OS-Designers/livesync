"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import typing
import builtins

import google.protobuf.message
import google.protobuf.descriptor
import google.protobuf.struct_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ConfigureRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SETTINGS_FIELD_NUMBER: builtins.int
    @property
    def settings(self) -> google.protobuf.struct_pb2.Struct: ...
    def __init__(
        self,
        *,
        settings: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["settings", b"settings"]) -> None: ...

global___ConfigureRequest = ConfigureRequest

@typing.final
class ConfigureResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    success: builtins.bool
    error_message: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["error_message", b"error_message", "success", b"success"]
    ) -> None: ...

global___ConfigureResponse = ConfigureResponse

@typing.final
class StepRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_FRAME_FIELD_NUMBER: builtins.int
    target_frame: builtins.bytes
    def __init__(
        self,
        *,
        target_frame: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["target_frame", b"target_frame"]) -> None: ...

global___StepRequest = StepRequest

@typing.final
class StepResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    PROCESSED_FRAME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    success: builtins.bool
    processed_frame: builtins.bytes
    error_message: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        processed_frame: builtins.bytes | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["_processed_frame", b"_processed_frame", "processed_frame", b"processed_frame"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_processed_frame",
            b"_processed_frame",
            "error_message",
            b"error_message",
            "processed_frame",
            b"processed_frame",
            "success",
            b"success",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["_processed_frame", b"_processed_frame"]
    ) -> typing.Literal["processed_frame"] | None: ...

global___StepResponse = StepResponse