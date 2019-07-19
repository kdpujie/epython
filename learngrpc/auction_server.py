#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟server'

__author__ = 'jie.pu'

import time
from concurrent import futures

import grpc

from learngrpc.proto.auto_auction_rpc_pb2_grpc import AutoAuctionServicer, add_AutoAuctionServicer_to_server
from learngrpc.proto.auto_auction_abi_pb2 import AutoResponse


_HOST = 'localhost'
_PORT = '6688'
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ActionService(AutoAuctionServicer):
    def auction(self, request, context):
        print(request)
        res = AutoResponse()
        res.request_id = request.request_id
        res.err_code = '200000'
        return res


def start_server():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_AutoAuctionServicer_to_server(ActionService(), grpc_server)
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)
    grpc_server.start()
    print('auction server启动完成')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    start_server()
