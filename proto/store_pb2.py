# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/store.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/store.proto\x12\x10\x64istributedstore\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\x0bPutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"+\n\x0bGetResponse\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x66ound\x18\x02 \x01(\x08\" \n\x11\x43\x61nCommitPetition\x12\x0b\n\x03key\x18\x01 \x01(\t\"&\n\x11\x43\x61nCommitResponse\x12\x11\n\tavailable\x18\x01 \x01(\x08\"$\n\x0cHaveCommited\x12\x14\n\x0chaveCommited\x18\x01 \x01(\x08\"\x1a\n\x0bVoteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\x0cVoteResponse\x12\x0c\n\x04vote\x18\x01 \x01(\x05\"\"\n\x0fSlowDownRequest\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\"#\n\x10SlowDownResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x10\n\x0eRestoreRequest\"\"\n\x0fRestoreResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"$\n\x12SlaveConfiguration\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\t\" \n\rNotifySuccess\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty2\xfc\x04\n\rKeyValueStore\x12\x42\n\x03put\x12\x1c.distributedstore.PutRequest\x1a\x1d.distributedstore.PutResponse\x12\x42\n\x03get\x12\x1c.distributedstore.GetRequest\x1a\x1d.distributedstore.GetResponse\x12U\n\tcanCommit\x12#.distributedstore.CanCommitPetition\x1a#.distributedstore.CanCommitResponse\x12H\n\x08\x64oCommit\x12\x1c.distributedstore.PutRequest\x1a\x1e.distributedstore.HaveCommited\x12H\n\x07\x61skVote\x12\x1d.distributedstore.VoteRequest\x1a\x1e.distributedstore.VoteResponse\x12Q\n\x08slowDown\x12!.distributedstore.SlowDownRequest\x1a\".distributedstore.SlowDownResponse\x12N\n\x07restore\x12 .distributedstore.RestoreRequest\x1a!.distributedstore.RestoreResponse\x12U\n\x0cnotifyMaster\x12$.distributedstore.SlaveConfiguration\x1a\x1f.distributedstore.NotifySuccessb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PUTREQUEST']._serialized_start=39
  _globals['_PUTREQUEST']._serialized_end=79
  _globals['_PUTRESPONSE']._serialized_start=81
  _globals['_PUTRESPONSE']._serialized_end=111
  _globals['_GETREQUEST']._serialized_start=113
  _globals['_GETREQUEST']._serialized_end=138
  _globals['_GETRESPONSE']._serialized_start=140
  _globals['_GETRESPONSE']._serialized_end=183
  _globals['_CANCOMMITPETITION']._serialized_start=185
  _globals['_CANCOMMITPETITION']._serialized_end=217
  _globals['_CANCOMMITRESPONSE']._serialized_start=219
  _globals['_CANCOMMITRESPONSE']._serialized_end=257
  _globals['_HAVECOMMITED']._serialized_start=259
  _globals['_HAVECOMMITED']._serialized_end=295
  _globals['_VOTEREQUEST']._serialized_start=297
  _globals['_VOTEREQUEST']._serialized_end=323
  _globals['_VOTERESPONSE']._serialized_start=325
  _globals['_VOTERESPONSE']._serialized_end=353
  _globals['_SLOWDOWNREQUEST']._serialized_start=355
  _globals['_SLOWDOWNREQUEST']._serialized_end=389
  _globals['_SLOWDOWNRESPONSE']._serialized_start=391
  _globals['_SLOWDOWNRESPONSE']._serialized_end=426
  _globals['_RESTOREREQUEST']._serialized_start=428
  _globals['_RESTOREREQUEST']._serialized_end=444
  _globals['_RESTORERESPONSE']._serialized_start=446
  _globals['_RESTORERESPONSE']._serialized_end=480
  _globals['_SLAVECONFIGURATION']._serialized_start=482
  _globals['_SLAVECONFIGURATION']._serialized_end=518
  _globals['_NOTIFYSUCCESS']._serialized_start=520
  _globals['_NOTIFYSUCCESS']._serialized_end=552
  _globals['_EMPTY']._serialized_start=554
  _globals['_EMPTY']._serialized_end=561
  _globals['_KEYVALUESTORE']._serialized_start=564
  _globals['_KEYVALUESTORE']._serialized_end=1200
# @@protoc_insertion_point(module_scope)
