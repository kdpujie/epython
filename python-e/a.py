#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

__author__ = 'pujie'

import sys
import pymysql
import xlrd
import jieba
import datetime

che_chi = []
result = {}


def test():
    args = sys.argv
    if len(args) == 1:
            print('Hello, world!', args)
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def test_time():
    start = datetime.datetime.strptime("2019-01", "%Y-%m")
    now = datetime.datetime.now()
    print(now.year - start.year)
    for w in jieba.cut("北京吉普"):
        print(w)
    a = [0 for i in range(5)]
    print(a)


def find_db():
    # 打开数据库连接
    db = pymysql.connect(host="10.4.8.2", port=20118, user="tmp_admin", password="123@456", db="aps_test",charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from crawl_online_auction where DATE_FORMAT(created_date,'%Y-%m-%d') = '2019-01-03'")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    for c in data:
        segmentation(c[3], c[28])
            # print("%s,%s,%s,%s,%s" % (c[1], c[2], c[3], c[5], c[16]))
    # 关闭数据库连接
    cursor.close()
    db.close()


def read_excel():
    book = xlrd.open_workbook('/Users/pujie/workspace/python/exercise/practice-file/车池0103.xlsx')  # 打开一个excel
    sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
    for i in sheet.get_rows():      # 获取每一行的数据
        serial = i[5].value
        if 2 == i[5].ctype:
            serial = str(int(serial))
        l1 = [i[3].value, serial]
        che_chi.append(l1)


def segmentation(title, url):
    for cc in che_chi:
        flag = False
        l = list(jieba.cut(cc[0]))
        for c in l:
            # c为车型 cc[1]为车系。包含车型和车系 则会匹配成功
            if (c not in "-") and (c in title) and (cc[1] in title):
                flag = True
                break
        if flag:
            key = cc[0] + " " + cc[1]
            record = [title, url]
            if result.__contains__(key):
                rr = result.get(key)
                rr.append(record)
                result[key] = rr
            else:
                result[key] = [record]


if __name__ == '__main__':
    test_time()
    # read_excel()
    # find_db()
    # for car, records in result.items():
    #     print(car)
    #     for r in records:
    #         print("\t %s, %s" % (r[0], r[1]))
    # find_db()