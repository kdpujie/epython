#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

__author__ = 'jie.pu'
from datetime import datetime,timedelta,timezone
import re


#把传入的时间，转换为指定时区的timstamp
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    n=re.match(r'UTC([+-]\d+):00',tz_str).group(1)
    n=int(n)
    utc_dt=dt.replace(tzinfo=timezone(timedelta(hours=n)))
    return utc_dt.timestamp()


def f1():
    now = datetime.now()
    print('str按时间格式转换成日期:',datetime.strptime('2015-6-1 08:10:30','%Y-%m-%d %H:%M:%S'))
    print('打印当前时间：',now.strftime('%Y-%m-%d %H:%M:%S'))
    print('当前时间+1hours+1minute：',now+timedelta(hours=1,minutes=1))
    print('当前的utc时间：',datetime.utcnow())
    print('时区转换：',to_timestamp('2015-6-1 08:10:30','UTC+7:00'))


if __name__ == '__main__':
    f1()