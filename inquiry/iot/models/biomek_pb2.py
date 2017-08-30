# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: biomek.proto

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
  name='biomek.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x62iomek.proto\"*\n\x12PlateReadingHeader\x12\x14\n\x0cplate_format\x18\x01 \x02(\t\"\x1e\n\x0bWellReading\x12\x0f\n\x07reading\x18\x01 \x02(\x02\"D\n\x0eWellReadingSet\x12\x12\n\nabsorbance\x18\x01 \x02(\x05\x12\x1e\n\x08readings\x18\x02 \x03(\x0b\x32\x0c.WellReading\"_\n\x0cPlateReading\x12#\n\x06header\x18\x01 \x02(\x0b\x32\x13.PlateReadingHeader\x12*\n\x11well_reading_sets\x18\x02 \x03(\x0b\x32\x0f.WellReadingSet\"\x11\n\x0f\x42ioMekRunconfig')
)




_PLATEREADINGHEADER = _descriptor.Descriptor(
  name='PlateReadingHeader',
  full_name='PlateReadingHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plate_format', full_name='PlateReadingHeader.plate_format', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=58,
)


_WELLREADING = _descriptor.Descriptor(
  name='WellReading',
  full_name='WellReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reading', full_name='WellReading.reading', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=90,
)


_WELLREADINGSET = _descriptor.Descriptor(
  name='WellReadingSet',
  full_name='WellReadingSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='absorbance', full_name='WellReadingSet.absorbance', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readings', full_name='WellReadingSet.readings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=160,
)


_PLATEREADING = _descriptor.Descriptor(
  name='PlateReading',
  full_name='PlateReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='PlateReading.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='well_reading_sets', full_name='PlateReading.well_reading_sets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=257,
)


_BIOMEKRUNCONFIG = _descriptor.Descriptor(
  name='BioMekRunconfig',
  full_name='BioMekRunconfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=276,
)

_WELLREADINGSET.fields_by_name['readings'].message_type = _WELLREADING
_PLATEREADING.fields_by_name['header'].message_type = _PLATEREADINGHEADER
_PLATEREADING.fields_by_name['well_reading_sets'].message_type = _WELLREADINGSET
DESCRIPTOR.message_types_by_name['PlateReadingHeader'] = _PLATEREADINGHEADER
DESCRIPTOR.message_types_by_name['WellReading'] = _WELLREADING
DESCRIPTOR.message_types_by_name['WellReadingSet'] = _WELLREADINGSET
DESCRIPTOR.message_types_by_name['PlateReading'] = _PLATEREADING
DESCRIPTOR.message_types_by_name['BioMekRunconfig'] = _BIOMEKRUNCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlateReadingHeader = _reflection.GeneratedProtocolMessageType('PlateReadingHeader', (_message.Message,), dict(
  DESCRIPTOR = _PLATEREADINGHEADER,
  __module__ = 'biomek_pb2'
  # @@protoc_insertion_point(class_scope:PlateReadingHeader)
  ))
_sym_db.RegisterMessage(PlateReadingHeader)

WellReading = _reflection.GeneratedProtocolMessageType('WellReading', (_message.Message,), dict(
  DESCRIPTOR = _WELLREADING,
  __module__ = 'biomek_pb2'
  # @@protoc_insertion_point(class_scope:WellReading)
  ))
_sym_db.RegisterMessage(WellReading)

WellReadingSet = _reflection.GeneratedProtocolMessageType('WellReadingSet', (_message.Message,), dict(
  DESCRIPTOR = _WELLREADINGSET,
  __module__ = 'biomek_pb2'
  # @@protoc_insertion_point(class_scope:WellReadingSet)
  ))
_sym_db.RegisterMessage(WellReadingSet)

PlateReading = _reflection.GeneratedProtocolMessageType('PlateReading', (_message.Message,), dict(
  DESCRIPTOR = _PLATEREADING,
  __module__ = 'biomek_pb2'
  # @@protoc_insertion_point(class_scope:PlateReading)
  ))
_sym_db.RegisterMessage(PlateReading)

BioMekRunconfig = _reflection.GeneratedProtocolMessageType('BioMekRunconfig', (_message.Message,), dict(
  DESCRIPTOR = _BIOMEKRUNCONFIG,
  __module__ = 'biomek_pb2'
  # @@protoc_insertion_point(class_scope:BioMekRunconfig)
  ))
_sym_db.RegisterMessage(BioMekRunconfig)


# @@protoc_insertion_point(module_scope)
