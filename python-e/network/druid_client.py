#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

from pydruid.client import *
from pydruid.utils.filters import Dimension
from pydruid.db import connect

query = PyDruid('http://192.168.177.212:8082', 'druid/v2')


def query_sql():
    conn = connect(host='druid-api.taoche.com', port=80, path='/druid/v2/sql/', scheme='http')
    curs = conn.cursor()
    curs.execute("""
    SELECT distinct car_id,series_id,spec_id, car_age,mileage,sale_price,data_source, sale_status,guide_price,
    sale_date, publish_date FROM alg_car_price_detail
    WHERE __time >= CURRENT_TIMESTAMP - INTERVAL '2' DAY  and data_source='guazi' and series_id=1825
    and mileage <10 and car_age < 8 and TIME_PARSE(publish_date) >= timestamp '2019-01-01 00:00:00' limit 20
    """)
    for row in curs:
        print(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8])


def query_scan():
    data = query.scan(
        datasource='alg_car_price_detail',
        granularity='none',
        intervals='2019-03-03/p1d',
        columns=['body_color', 'city_id'],
        filter=(Dimension('brand_name') == '上汽大众'),
        limit=10
    )
    print(json.dumps(data.query_dict, indent=2))
    df = query.export_pandas()
    print(len(df))
    for i in range(len(df)):
        print(df.loc[i, :])


if __name__ == '__main__':
    query_sql()