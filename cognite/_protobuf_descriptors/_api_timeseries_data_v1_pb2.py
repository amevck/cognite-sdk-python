# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_timeseries_data_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api_timeseries_data_v1.proto',
  package='api',
  syntax='proto3',
  serialized_pb=_b('\n\x1c\x61pi_timeseries_data_v1.proto\x12\x03\x61pi\"3\n\x0fStringDatapoint\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t\"4\n\x10NumericDatapoint\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x01\"<\n\x14StringTimeseriesData\x12$\n\x06points\x18\x01 \x03(\x0b\x32\x14.api.StringDatapoint\">\n\x15NumericTimeseriesData\x12%\n\x06points\x18\x01 \x03(\x0b\x32\x15.api.NumericDatapoint\"|\n\x0eTimeseriesData\x12/\n\nstringData\x18\x01 \x01(\x0b\x32\x19.api.StringTimeseriesDataH\x00\x12\x31\n\x0bnumericData\x18\x02 \x01(\x0b\x32\x1a.api.NumericTimeseriesDataH\x00\x42\x06\n\x04\x64\x61ta\"\x8e\x01\n\x11TagTimeseriesData\x12\r\n\x05tagId\x18\x01 \x01(\t\x12/\n\nstringData\x18\x02 \x01(\x0b\x32\x19.api.StringTimeseriesDataH\x00\x12\x31\n\x0bnumericData\x18\x03 \x01(\x0b\x32\x1a.api.NumericTimeseriesDataH\x00\x42\x06\n\x04\x64\x61ta\"K\n\x16MultiTagTimeseriesData\x12\x31\n\x11tagTimeseriesData\x18\x01 \x03(\x0b\x32\x16.api.TagTimeseriesDataB4\n\x17\x63om.cognite.data.api.v1P\x01\xb8\x01\x01\xaa\x02\x13\x43ognite.Data.Api.V1b\x06proto3')
)




_STRINGDATAPOINT = _descriptor.Descriptor(
  name='StringDatapoint',
  full_name='api.StringDatapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.StringDatapoint.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.StringDatapoint.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=88,
)


_NUMERICDATAPOINT = _descriptor.Descriptor(
  name='NumericDatapoint',
  full_name='api.NumericDatapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='api.NumericDatapoint.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.NumericDatapoint.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=142,
)


_STRINGTIMESERIESDATA = _descriptor.Descriptor(
  name='StringTimeseriesData',
  full_name='api.StringTimeseriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='api.StringTimeseriesData.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=204,
)


_NUMERICTIMESERIESDATA = _descriptor.Descriptor(
  name='NumericTimeseriesData',
  full_name='api.NumericTimeseriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='api.NumericTimeseriesData.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=268,
)


_TIMESERIESDATA = _descriptor.Descriptor(
  name='TimeseriesData',
  full_name='api.TimeseriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stringData', full_name='api.TimeseriesData.stringData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numericData', full_name='api.TimeseriesData.numericData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='api.TimeseriesData.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=270,
  serialized_end=394,
)


_TAGTIMESERIESDATA = _descriptor.Descriptor(
  name='TagTimeseriesData',
  full_name='api.TagTimeseriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tagId', full_name='api.TagTimeseriesData.tagId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stringData', full_name='api.TagTimeseriesData.stringData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numericData', full_name='api.TagTimeseriesData.numericData', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='api.TagTimeseriesData.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=397,
  serialized_end=539,
)


_MULTITAGTIMESERIESDATA = _descriptor.Descriptor(
  name='MultiTagTimeseriesData',
  full_name='api.MultiTagTimeseriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tagTimeseriesData', full_name='api.MultiTagTimeseriesData.tagTimeseriesData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=616,
)

_STRINGTIMESERIESDATA.fields_by_name['points'].message_type = _STRINGDATAPOINT
_NUMERICTIMESERIESDATA.fields_by_name['points'].message_type = _NUMERICDATAPOINT
_TIMESERIESDATA.fields_by_name['stringData'].message_type = _STRINGTIMESERIESDATA
_TIMESERIESDATA.fields_by_name['numericData'].message_type = _NUMERICTIMESERIESDATA
_TIMESERIESDATA.oneofs_by_name['data'].fields.append(
  _TIMESERIESDATA.fields_by_name['stringData'])
_TIMESERIESDATA.fields_by_name['stringData'].containing_oneof = _TIMESERIESDATA.oneofs_by_name['data']
_TIMESERIESDATA.oneofs_by_name['data'].fields.append(
  _TIMESERIESDATA.fields_by_name['numericData'])
_TIMESERIESDATA.fields_by_name['numericData'].containing_oneof = _TIMESERIESDATA.oneofs_by_name['data']
_TAGTIMESERIESDATA.fields_by_name['stringData'].message_type = _STRINGTIMESERIESDATA
_TAGTIMESERIESDATA.fields_by_name['numericData'].message_type = _NUMERICTIMESERIESDATA
_TAGTIMESERIESDATA.oneofs_by_name['data'].fields.append(
  _TAGTIMESERIESDATA.fields_by_name['stringData'])
_TAGTIMESERIESDATA.fields_by_name['stringData'].containing_oneof = _TAGTIMESERIESDATA.oneofs_by_name['data']
_TAGTIMESERIESDATA.oneofs_by_name['data'].fields.append(
  _TAGTIMESERIESDATA.fields_by_name['numericData'])
_TAGTIMESERIESDATA.fields_by_name['numericData'].containing_oneof = _TAGTIMESERIESDATA.oneofs_by_name['data']
_MULTITAGTIMESERIESDATA.fields_by_name['tagTimeseriesData'].message_type = _TAGTIMESERIESDATA
DESCRIPTOR.message_types_by_name['StringDatapoint'] = _STRINGDATAPOINT
DESCRIPTOR.message_types_by_name['NumericDatapoint'] = _NUMERICDATAPOINT
DESCRIPTOR.message_types_by_name['StringTimeseriesData'] = _STRINGTIMESERIESDATA
DESCRIPTOR.message_types_by_name['NumericTimeseriesData'] = _NUMERICTIMESERIESDATA
DESCRIPTOR.message_types_by_name['TimeseriesData'] = _TIMESERIESDATA
DESCRIPTOR.message_types_by_name['TagTimeseriesData'] = _TAGTIMESERIESDATA
DESCRIPTOR.message_types_by_name['MultiTagTimeseriesData'] = _MULTITAGTIMESERIESDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringDatapoint = _reflection.GeneratedProtocolMessageType('StringDatapoint', (_message.Message,), dict(
  DESCRIPTOR = _STRINGDATAPOINT,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.StringDatapoint)
  ))
_sym_db.RegisterMessage(StringDatapoint)

NumericDatapoint = _reflection.GeneratedProtocolMessageType('NumericDatapoint', (_message.Message,), dict(
  DESCRIPTOR = _NUMERICDATAPOINT,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.NumericDatapoint)
  ))
_sym_db.RegisterMessage(NumericDatapoint)

StringTimeseriesData = _reflection.GeneratedProtocolMessageType('StringTimeseriesData', (_message.Message,), dict(
  DESCRIPTOR = _STRINGTIMESERIESDATA,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.StringTimeseriesData)
  ))
_sym_db.RegisterMessage(StringTimeseriesData)

NumericTimeseriesData = _reflection.GeneratedProtocolMessageType('NumericTimeseriesData', (_message.Message,), dict(
  DESCRIPTOR = _NUMERICTIMESERIESDATA,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.NumericTimeseriesData)
  ))
_sym_db.RegisterMessage(NumericTimeseriesData)

TimeseriesData = _reflection.GeneratedProtocolMessageType('TimeseriesData', (_message.Message,), dict(
  DESCRIPTOR = _TIMESERIESDATA,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.TimeseriesData)
  ))
_sym_db.RegisterMessage(TimeseriesData)

TagTimeseriesData = _reflection.GeneratedProtocolMessageType('TagTimeseriesData', (_message.Message,), dict(
  DESCRIPTOR = _TAGTIMESERIESDATA,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.TagTimeseriesData)
  ))
_sym_db.RegisterMessage(TagTimeseriesData)

MultiTagTimeseriesData = _reflection.GeneratedProtocolMessageType('MultiTagTimeseriesData', (_message.Message,), dict(
  DESCRIPTOR = _MULTITAGTIMESERIESDATA,
  __module__ = 'api_timeseries_data_v1_pb2'
  # @@protoc_insertion_point(class_scope:api.MultiTagTimeseriesData)
  ))
_sym_db.RegisterMessage(MultiTagTimeseriesData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.cognite.data.api.v1P\001\270\001\001\252\002\023Cognite.Data.Api.V1'))
# @@protoc_insertion_point(module_scope)