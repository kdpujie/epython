#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

__author__ = 'jie.pu'

import logging
from kafka import KafkaProducer
from learngrpc import pb_test
logging.basicConfig(level=logging.INFO)  #日志级别debug，info，warning，error

topic = 'test'


def kafka_producer():
    p = KafkaProducer(bootstrap_servers=['10.130.138.164:9092'])
    p.send(topic, 'value is haha'.encode('utf-8'))
    for i in range(1,10):
        message_str = 'kafka message from python: index={i}'.format(i=i)
        response = p.send(topic, message_str.encode('utf-8'))
        print(response)
    p.flush()
    p.close()


def send_search_log():
    p = KafkaProducer(bootstrap_servers=['10.130.138.164:9092'])
    sl = pb_test.generate_search_log()
    response = p.send(topic, sl.SerializeToString())
    print(response)
    p.flush()
    p.close()


if __name__ == '__main__':
    send_search_log()
