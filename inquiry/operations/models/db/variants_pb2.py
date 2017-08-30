# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: variants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='variants.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0evariants.proto\x1a\x0c\x63ommon.proto\"\x90\x01\n\x12VariantSetMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0e\n\x06number\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x1f\n\nattributes\x18\x08 \x01(\x0b\x32\x0b.Attributes\"{\n\nVariantSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12\x18\n\x10reference_set_id\x18\x04 \x01(\t\x12%\n\x08metadata\x18\x05 \x03(\x0b\x32\x13.VariantSetMetadata\"\x95\x01\n\x07\x43\x61llSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x03 \x01(\t\x12\x17\n\x0fvariant_set_ids\x18\x04 \x03(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\x03\x12\x0f\n\x07updated\x18\x06 \x01(\x03\x12\x1f\n\nattributes\x18\x08 \x01(\x0b\x32\x0b.Attributes\"\xa0\x01\n\x04\x43\x61ll\x12\x15\n\rcall_set_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61ll_set_id\x18\x02 \x01(\t\x12\x1c\n\x08genotype\x18\x07 \x01(\x0b\x32\n.ListValue\x12\x10\n\x08phaseset\x18\x04 \x01(\t\x12\x1b\n\x13genotype_likelihood\x18\x05 \x03(\x01\x12\x1f\n\nattributes\x18\x08 \x01(\x0b\x32\x0b.Attributes\"\x87\x03\n\x07Variant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0evariant_set_id\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x03\x12\x0f\n\x07updated\x18\x05 \x01(\x03\x12\x16\n\x0ereference_name\x18\x06 \x01(\t\x12\r\n\x05start\x18\x07 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x08 \x01(\x03\x12\x17\n\x0freference_bases\x18\t \x01(\t\x12\x17\n\x0f\x61lternate_bases\x18\n \x03(\t\x12\x1f\n\nattributes\x18\r \x01(\x0b\x32\x0b.Attributes\x12\x14\n\x05\x63\x61lls\x18\x0c \x03(\x0b\x32\x05.Call\x12\x14\n\x0cvariant_type\x18\x11 \x01(\t\x12\r\n\x05svlen\x18\x12 \x01(\x03\x12\r\n\x05\x63ipos\x18\x13 \x03(\x11\x12\r\n\x05\x63iend\x18\x14 \x03(\x11\x12\x17\n\x0f\x66ilters_applied\x18\x0e \x01(\x08\x12\x16\n\x0e\x66ilters_passed\x18\x0f \x01(\x08\x12\x16\n\x0e\x66ilters_failed\x18\x10 \x03(\tb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_VARIANTSETMETADATA = _descriptor.Descriptor(
  name='VariantSetMetadata',
  full_name='VariantSetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='VariantSetMetadata.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='VariantSetMetadata.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='VariantSetMetadata.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='VariantSetMetadata.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='VariantSetMetadata.number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='VariantSetMetadata.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='VariantSetMetadata.attributes', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=177,
)


_VARIANTSET = _descriptor.Descriptor(
  name='VariantSet',
  full_name='VariantSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='VariantSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='VariantSet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='VariantSet.dataset_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='VariantSet.reference_set_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='VariantSet.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=302,
)


_CALLSET = _descriptor.Descriptor(
  name='CallSet',
  full_name='CallSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CallSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='CallSet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='CallSet.biosample_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_set_ids', full_name='CallSet.variant_set_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='CallSet.created', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='CallSet.updated', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='CallSet.attributes', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=454,
)


_CALL = _descriptor.Descriptor(
  name='Call',
  full_name='Call',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_set_name', full_name='Call.call_set_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_id', full_name='Call.call_set_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotype', full_name='Call.genotype', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phaseset', full_name='Call.phaseset', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotype_likelihood', full_name='Call.genotype_likelihood', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='Call.attributes', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=617,
)


_VARIANT = _descriptor.Descriptor(
  name='Variant',
  full_name='Variant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Variant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='Variant.variant_set_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='Variant.names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='Variant.created', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='Variant.updated', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='Variant.reference_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='Variant.start', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='Variant.end', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_bases', full_name='Variant.reference_bases', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bases', full_name='Variant.alternate_bases', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='Variant.attributes', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calls', full_name='Variant.calls', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_type', full_name='Variant.variant_type', index=12,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svlen', full_name='Variant.svlen', index=13,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cipos', full_name='Variant.cipos', index=14,
      number=19, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ciend', full_name='Variant.ciend', index=15,
      number=20, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_applied', full_name='Variant.filters_applied', index=16,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_passed', full_name='Variant.filters_passed', index=17,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters_failed', full_name='Variant.filters_failed', index=18,
      number=16, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=1011,
)

_VARIANTSETMETADATA.fields_by_name['attributes'].message_type = common__pb2._ATTRIBUTES
_VARIANTSET.fields_by_name['metadata'].message_type = _VARIANTSETMETADATA
_CALLSET.fields_by_name['attributes'].message_type = common__pb2._ATTRIBUTES
_CALL.fields_by_name['genotype'].message_type = common__pb2._LISTVALUE
_CALL.fields_by_name['attributes'].message_type = common__pb2._ATTRIBUTES
_VARIANT.fields_by_name['attributes'].message_type = common__pb2._ATTRIBUTES
_VARIANT.fields_by_name['calls'].message_type = _CALL
DESCRIPTOR.message_types_by_name['VariantSetMetadata'] = _VARIANTSETMETADATA
DESCRIPTOR.message_types_by_name['VariantSet'] = _VARIANTSET
DESCRIPTOR.message_types_by_name['CallSet'] = _CALLSET
DESCRIPTOR.message_types_by_name['Call'] = _CALL
DESCRIPTOR.message_types_by_name['Variant'] = _VARIANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VariantSetMetadata = _reflection.GeneratedProtocolMessageType('VariantSetMetadata', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTSETMETADATA,
  __module__ = 'variants_pb2'
  # @@protoc_insertion_point(class_scope:VariantSetMetadata)
  ))
_sym_db.RegisterMessage(VariantSetMetadata)

VariantSet = _reflection.GeneratedProtocolMessageType('VariantSet', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTSET,
  __module__ = 'variants_pb2'
  # @@protoc_insertion_point(class_scope:VariantSet)
  ))
_sym_db.RegisterMessage(VariantSet)

CallSet = _reflection.GeneratedProtocolMessageType('CallSet', (_message.Message,), dict(
  DESCRIPTOR = _CALLSET,
  __module__ = 'variants_pb2'
  # @@protoc_insertion_point(class_scope:CallSet)
  ))
_sym_db.RegisterMessage(CallSet)

Call = _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), dict(
  DESCRIPTOR = _CALL,
  __module__ = 'variants_pb2'
  # @@protoc_insertion_point(class_scope:Call)
  ))
_sym_db.RegisterMessage(Call)

Variant = _reflection.GeneratedProtocolMessageType('Variant', (_message.Message,), dict(
  DESCRIPTOR = _VARIANT,
  __module__ = 'variants_pb2'
  # @@protoc_insertion_point(class_scope:Variant)
  ))
_sym_db.RegisterMessage(Variant)


# @@protoc_insertion_point(module_scope)
