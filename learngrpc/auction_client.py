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

_HOST = '192.168.165.134'
_PORT = '6677'


def generate_request(req_pre):
    number = 5
    for i in range(number):
        req = AutoRequest()
        req.request_id = f'req_id_{req_pre}_{i}'
        now = datetime.datetime.now().timetuple()
        req.timestamp = int(time.mktime(now))
        if i == number - 1:
            req.req_type = '2'
            req.youxin.max_total_price = 5.88
            req.youxin.current_total_price = 5.68
            req.youxin.deal_status = '未成交'
        else:
            req.req_type = '1'
        req.youxin.current_total_price = 5.08
        req.youxin.vehicle_id = 'B03137049'
        req.youxin.current_quote_price = 4.98
        req.youxin.steps.append(200)
        req.youxin.steps.append(500)
        req.youxin.is_first_price = False
        req.youxin.is_arrive_reserve_price = 0
        # print(f'request: {req}')
        yield req


def call_server(req_pre):
    # requests = generate_request(req_pre)
    # for req in requests:
    #     print(req.youxin.steps[0])
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
    call_server('thread')
    # for i in generate_request():
    #     print(i)
