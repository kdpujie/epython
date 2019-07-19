#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟client'

__author__ = 'jie.pu'

import grpc
from learngrpc.proto.auto_auction_rpc_pb2_grpc import AutoAuctionStub
from learngrpc.proto.auto_auction_abi_pb2 import AutoRequest

_HOST = 'localhost'
_PORT = '6688'


def start_server():
    req = AutoRequest()
    req.request_id = 'res_id_00001111'
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = AutoAuctionStub(channel=conn)
    response = client.auction(req)
    print(response)


if __name__ == '__main__':
    start_server()
