#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟server'

__author__ = 'jie.pu'

import time
from concurrent import futures

import grpc

from learngrpc.proto import sigmob_jion_pb2, sigmob_jion_pb2_grpc

_HOST = 'localhost'
_PORT = '6688'
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RtbService(sigmob_jion_pb2_grpc.RtbServicer):
    def GetMobileAd(self, request, context):
        print(request)
        res = sigmob_jion_pb2.SearchLog()
        res.sid = 'res_id_00001111'
        res.error_code = 200000
        return res


def start_server():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    sigmob_jion_pb2_grpc.add_RtbServicer_to_server(RtbService(), grpc_server)
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)
    grpc_server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    start_server()