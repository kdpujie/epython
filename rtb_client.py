#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟client'

__author__ = 'jie.pu'

import grpc
from learngrpc.proto import sigmob_jion_pb2, sigmob_jion_pb2_grpc

_HOST = 'localhost'
_PORT = '6688'


def generate_search_log():
    sl = sigmob_jion_pb2.SearchLog()
    sl.sid = 'req_001'
    return sl


def start_server():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = sigmob_jion_pb2_grpc.RtbStub(channel=conn)
    response = client.GetMobileAd(sigmob_jion_pb2.SearchLog(sid='req_12124'))
    print(response)


if __name__ == '__main__':
    start_server()