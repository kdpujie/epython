#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

import json
import requests


def test_json():
    """{
        "vehicleModelId": "12834",
        "provinceId": 110000,
        "cityId": 110100,
        "carRegDate": "2016-11-01",
        "mileage": 2.0,
        "colorName": "黑色",
        "transferTimes": 1,
        "userName": "15101013237",
        "channel": "taochejian",
        "token": "",
        "unifiedNumber": "000534783",
        "pid": 1,
        "applySalePrice":805345,
        "isTest":0
    }"""
    payload = {'vehicleModelId': 'data', 'A':'a'}
    data = json.dumps(payload)
    print(data)


def http_send():
    url = ""
    requests.post(url)


if __name__ == '__main__':
    test_json()