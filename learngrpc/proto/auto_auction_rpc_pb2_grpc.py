# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import learngrpc.proto.auto_auction_rpc_pb2 as auto__auction__rpc__pb2


class AutoAuctionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.auction = channel.stream_stream(
        '/auction.AutoAuction/auction',
        request_serializer=auto__auction__rpc__pb2.AutoRequest.SerializeToString,
        response_deserializer=auto__auction__rpc__pb2.AutoResponse.FromString,
        )


class AutoAuctionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def auction(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AutoAuctionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'auction': grpc.stream_stream_rpc_method_handler(
          servicer.auction,
          request_deserializer=auto__auction__rpc__pb2.AutoRequest.FromString,
          response_serializer=auto__auction__rpc__pb2.AutoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'auction.AutoAuction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
