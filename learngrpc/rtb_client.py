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
    sl.timestamp = 154353452
    sl.uid = "uid_00001"
    sl.channel_id = "1"

    req = sl.request
    req.request_id = "req_id_00001"

    app = req.app
    app.app_id = "app_id_001"
    app.app_package = "com.sigmob.animal"
    app.name = "开心消消乐"
    app.app_version.major = 4
    app.app_version.minor = 2
    app.app_version.micro = 0

    dev = req.device
    dev.device_type = 1
    dev.os_type = 1
    dev.os_version.major = 9
    dev.os_version.minor = 2
    dev.os_version.micro = 1
    dev.vendor = "小米科技"
    dev.model = "MI note 2"
    dev.did.idfa = "idfa_2323465"
    dev.did.udid = "udid_adgasdf"

    net = req.network
    net.ipv4 = "61.49.51.159"
    net.connection_type = 100

    slot = req.slots.add()
    slot.adslot_id = "slot_id_001"
    slot.adslot_type.append(1)
    slot.bidfloor = 90
    slot.vid = "vid_3s5h2s3451a23asdf23ad"
    return sl


def start_server():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = sigmob_jion_pb2_grpc.RtbStub(channel=conn)
    response = client.GetMobileAd(generate_search_log())
    print(response)


if __name__ == '__main__':
    start_server()