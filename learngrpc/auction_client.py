#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'rtb 服务的模拟client'

__author__ = 'jie.pu'

import _thread
import time
import datetime

import grpc
from learngrpc.proto.auto_auction_rpc_pb2_grpc import AutoAuctionStub
from learngrpc.proto.auto_auction_abi_pb2 import AutoRequest

_HOST = 'localhost'
_PORT = '6688'


def generate_request(req_pre):
    number = 5
    for i in range(number):
        req = AutoRequest()
        req.request_id = f'req_id_{req_pre}_{i}'
        now = datetime.datetime.now().timetuple()
        req.timestamp = int(time.mktime(now))
        if i == number - 1:
            req.req_type = '2'
        else:
            req.req_type = '1'
        req.youxin.current_total_price = 5.08
        # print(f'request: {req}')
        yield req


def call_server(req_pre):
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = AutoAuctionStub(channel=conn)
    responses = client.auction(generate_request(req_pre))
    for res in responses:
        print(f'response: {res}')


def multi_call():
    try:
        _thread.start_new_thread(call_server, ("thread-1", ))
        _thread.start_new_thread(call_server, ("thread-2", ))
    except Exception:
        print("Error: unable to start thread")
    while 1:
        pass


if __name__ == '__main__':
    multi_call()
    # for i in generate_request():
    #     print(i)
