#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

__author__ = 'jie.pu'

import logging
from kafka import KafkaConsumer
from learngrpc.proto import sigmob_jion_pb2
logging.basicConfig(level=logging.INFO, #日志级别debug，info，warning，error
                    filename="consumer.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
topic = 'test'
group_id = 'test'
brokers = ['10.130.138.164:9092']


def kafka_subscribe():
    try:
        c = KafkaConsumer(
            topic,
            group_id = group_id,
            bootstrap_servers = brokers,
        )
    except BaseException as e:
        logging.exception(e)
    else:
        for msg in c:
            sl = sigmob_jion_pb2.SearchLog()
            sl.ParseFromString(msg.value)
            logging.info(sl)


if __name__ == '__main__':
    kafka_subscribe()