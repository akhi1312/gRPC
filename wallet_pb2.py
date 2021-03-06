# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet.proto

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
  name='wallet.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cwallet.proto\"Q\n\x04\x43\x61rd\x12\x18\n\x10\x63\x61rd_holder_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61rd_number\x18\x02 \x01(\t\x12\x1a\n\x12\x63\x61rd_expiry_yyyymm\x18\x03 \x01(\x05\")\n\x12\x43\x61rdEncryptRequest\x12\x13\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\x05.Card\"$\n\x13\x43\x61rdEncryptResponse\x12\r\n\x05token\x18\x01 \x01(\t\"#\n\x12\x43\x61rdDecryptRequest\x12\r\n\x05token\x18\x01 \x01(\t\"1\n\x13\x43\x61rdDecryptResponse\x12\x1a\n\x12\x63\x61rd_in_plain_text\x18\x01 \x01(\t2x\n\x06Wallet\x12\x36\n\x07\x65ncrypt\x12\x13.CardEncryptRequest\x1a\x14.CardEncryptResponse\"\x00\x12\x36\n\x07\x64\x65\x63rypt\x12\x13.CardDecryptRequest\x1a\x14.CardDecryptResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_holder_name', full_name='Card.card_holder_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_number', full_name='Card.card_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_expiry_yyyymm', full_name='Card.card_expiry_yyyymm', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=16,
  serialized_end=97,
)


_CARDENCRYPTREQUEST = _descriptor.Descriptor(
  name='CardEncryptRequest',
  full_name='CardEncryptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card', full_name='CardEncryptRequest.card', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=99,
  serialized_end=140,
)


_CARDENCRYPTRESPONSE = _descriptor.Descriptor(
  name='CardEncryptResponse',
  full_name='CardEncryptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='CardEncryptResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=178,
)


_CARDDECRYPTREQUEST = _descriptor.Descriptor(
  name='CardDecryptRequest',
  full_name='CardDecryptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='CardDecryptRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=215,
)


_CARDDECRYPTRESPONSE = _descriptor.Descriptor(
  name='CardDecryptResponse',
  full_name='CardDecryptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_in_plain_text', full_name='CardDecryptResponse.card_in_plain_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=266,
)

_CARDENCRYPTREQUEST.fields_by_name['card'].message_type = _CARD
DESCRIPTOR.message_types_by_name['Card'] = _CARD
DESCRIPTOR.message_types_by_name['CardEncryptRequest'] = _CARDENCRYPTREQUEST
DESCRIPTOR.message_types_by_name['CardEncryptResponse'] = _CARDENCRYPTRESPONSE
DESCRIPTOR.message_types_by_name['CardDecryptRequest'] = _CARDDECRYPTREQUEST
DESCRIPTOR.message_types_by_name['CardDecryptResponse'] = _CARDDECRYPTRESPONSE

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), dict(
  DESCRIPTOR = _CARD,
  __module__ = 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:Card)
  ))
_sym_db.RegisterMessage(Card)

CardEncryptRequest = _reflection.GeneratedProtocolMessageType('CardEncryptRequest', (_message.Message,), dict(
  DESCRIPTOR = _CARDENCRYPTREQUEST,
  __module__ = 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:CardEncryptRequest)
  ))
_sym_db.RegisterMessage(CardEncryptRequest)

CardEncryptResponse = _reflection.GeneratedProtocolMessageType('CardEncryptResponse', (_message.Message,), dict(
  DESCRIPTOR = _CARDENCRYPTRESPONSE,
  __module__ = 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:CardEncryptResponse)
  ))
_sym_db.RegisterMessage(CardEncryptResponse)

CardDecryptRequest = _reflection.GeneratedProtocolMessageType('CardDecryptRequest', (_message.Message,), dict(
  DESCRIPTOR = _CARDDECRYPTREQUEST,
  __module__ = 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:CardDecryptRequest)
  ))
_sym_db.RegisterMessage(CardDecryptRequest)

CardDecryptResponse = _reflection.GeneratedProtocolMessageType('CardDecryptResponse', (_message.Message,), dict(
  DESCRIPTOR = _CARDDECRYPTRESPONSE,
  __module__ = 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:CardDecryptResponse)
  ))
_sym_db.RegisterMessage(CardDecryptResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class WalletStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.encrypt = channel.unary_unary(
          '/Wallet/encrypt',
          request_serializer=CardEncryptRequest.SerializeToString,
          response_deserializer=CardEncryptResponse.FromString,
          )
      self.decrypt = channel.unary_unary(
          '/Wallet/decrypt',
          request_serializer=CardDecryptRequest.SerializeToString,
          response_deserializer=CardDecryptResponse.FromString,
          )


  class WalletServicer(object):

    def encrypt(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def decrypt(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_WalletServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'encrypt': grpc.unary_unary_rpc_method_handler(
            servicer.encrypt,
            request_deserializer=CardEncryptRequest.FromString,
            response_serializer=CardEncryptResponse.SerializeToString,
        ),
        'decrypt': grpc.unary_unary_rpc_method_handler(
            servicer.decrypt,
            request_deserializer=CardDecryptRequest.FromString,
            response_serializer=CardDecryptResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Wallet', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaWalletServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def encrypt(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def decrypt(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaWalletStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def encrypt(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    encrypt.future = None
    def decrypt(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    decrypt.future = None


  def beta_create_Wallet_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Wallet', 'decrypt'): CardDecryptRequest.FromString,
      ('Wallet', 'encrypt'): CardEncryptRequest.FromString,
    }
    response_serializers = {
      ('Wallet', 'decrypt'): CardDecryptResponse.SerializeToString,
      ('Wallet', 'encrypt'): CardEncryptResponse.SerializeToString,
    }
    method_implementations = {
      ('Wallet', 'decrypt'): face_utilities.unary_unary_inline(servicer.decrypt),
      ('Wallet', 'encrypt'): face_utilities.unary_unary_inline(servicer.encrypt),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Wallet_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Wallet', 'decrypt'): CardDecryptRequest.SerializeToString,
      ('Wallet', 'encrypt'): CardEncryptRequest.SerializeToString,
    }
    response_deserializers = {
      ('Wallet', 'decrypt'): CardDecryptResponse.FromString,
      ('Wallet', 'encrypt'): CardEncryptResponse.FromString,
    }
    cardinalities = {
      'decrypt': cardinality.Cardinality.UNARY_UNARY,
      'encrypt': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Wallet', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
