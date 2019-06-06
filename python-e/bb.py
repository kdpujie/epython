# -*- coding: utf-8 -*-
"""
Created on 2019/4/9 10:15
@Author: haoqianqiong
Keep Walking!!!
选取近似车况的同车型（后续可扩大至同年款）同省份车辆，
门店	省份id	车型名称	mileage	reg_date	price	spec_id
"""

import time
import datetime
import grpc
import sys, traceback
import sys
import json
from pydruid.client import *
from pydruid.db import connect
from pydruid.utils.filters import Dimension
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")


def get_data(conn, spec_id, prov):
    start = datetime.datetime.now()
    limit = 600
    print("******'{}'*******'{}'*****".format(spec_id,prov))
    try:
        today = datetime.datetime.now()
        delta = datetime.timedelta(days=120)
        day = today - delta
        date_from = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
        date_from = date_from.strftime("%Y-%m-%d %H:%M:%S")
        sql1 = """ SELECT distinct car_id,series_id,spec_id, cast(car_age as double) as car_age,
            cast(mileage as double) as mileage,data_source,cast(sale_status as int) as sale_status,
            (case when if_ensure_sale = 1 then cast(sale_price as double)*1.05 else cast(sale_price as double) * 0.98 end) as sale_price,
            cast(guide_price as double) as guide_price, sale_date, publish_date as pub_date,
            plate_first_date, vehicle_url
            FROM alg_car_price_detail
            WHERE __time >= CURRENT_TIMESTAMP - INTERVAL '1' DAY  and data_source='guazi' 
            and spec_id='{}'  and mileage <10 and car_age < 8 and if_ensure_sale = 1
            and province_id in {}  and TIME_PARSE(publish_date) >= timestamp '{}'
            limit {}
            """.format(spec_id, prov, date_from, limit)
        print("1111")
        curs1 = conn.cursor()
        print("22222")
        curs1.execute(sql1)
        print("33333")
        data1 = curs1.fetchall()
        print("44444")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print
        "*** print sys.exc_info:"
        print
        'exc_type is: %s, exc_value is: %s, exc_traceback is: %s' % (exc_type, exc_value, exc_traceback)
        print
        "-" * 100

        print
        "*** print_tb:"
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        print
        "-" * 100

        print
        "*** print_exception:"
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
        print
        "-" * 100

        print
        "*** print_exc:"
        traceback.print_exc()
        print
        "-" * 100

        print
        "*** format_exc, first and last line:"
        formatted_lines = traceback.format_exc().splitlines()
        print
        formatted_lines[0]
        print
        formatted_lines[-1]
        print
        "-" * 100

        print
        "*** format_exception:"
        print
        repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print
        "-" * 100

        print
        "*** extract_tb:"
        print
        repr(traceback.extract_tb(exc_traceback))
        print
        "-" * 100

        print
        "*** extract_stack:"
        print
        traceback.extract_stack()
        print
        "-" * 100

        print
        "*** format_tb:"
        print
        repr(traceback.format_tb(exc_traceback))
        print
        "-" * 100

        print
        "*** tb_lineno:", exc_traceback.tb_lineno

        print
        traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'), ('eggs.py', 42, 'eggs', 'return "bacon"')])
        print('异常:', e)
    finally:
        curs1.close()
        print("查询耗时：%d s；sql：%s" % ((datetime.datetime.now() - start).seconds, sql1))
    return data1


def detectoutliers(list):
    Q1 = np.percentile(list, 25)
    Q3 = np.percentile(list, 75)
    IQR = Q3 - Q1
    outlier_step = 1.1 * IQR
    lower_limit = Q1 - outlier_step
    upper_limit = Q3 + outlier_step
    return lower_limit, upper_limit


def df_change(df):
    start_time11 = datetime.datetime.now()
    b_data = df['sale_price']
    print('before change:', df.shape)
    lower_limit, upper_limit = detectoutliers(b_data)
    index = df[(df['sale_price'] <= lower_limit) | (df['sale_price'] >= upper_limit)].index.tolist()
    for i in index:
        j = float(i)
        df.drop(j, axis=0, inplace=True)
    df.rename(columns={'sale_price': 'price'}, inplace=True)
    df['used_days'] = (
            df['sale_date'].apply(lambda x: pd.to_datetime(x)) -
            df['plate_first_date'].apply(lambda x: pd.to_datetime(x))
    ).apply(lambda x: x.days)
    df['car_age'] = df['used_days'] / 365
    print("get total items costs:", (datetime.datetime.now() - start_time11))
    print('data_preprocess after change:', df.shape)
    return df


def low_up(car_age, age_diff, mileage, mile_diff):
    upper_age = car_age + age_diff
    if car_age < 1.5:
        lower_age = 0
    else:
        lower_age = car_age - age_diff
    print("lower_age and upper_age are:", lower_age, upper_age)

    upper_mile = mileage + mile_diff
    if mileage < 1.5:
        lower_mile = 0
    else:
        lower_mile = mileage - mile_diff
    print("lower_mile and upper_mile are:", lower_mile, upper_mile)
    return lower_age, upper_age, lower_mile, upper_mile


if __name__ == '__main__':
    # shop_id, province_id, spec_name, mileage, reg_date, price, spec_id, car_age
    data_f = pd.read_excel(r'/Users/pujie/Desktop/selling_190527.xlsx', header=None)
    the_result = []
    kkk = 0
    conn = connect(host='druid-api.taoche.com', port=80, path='/druid/v2/sql/', scheme='http')
    for i in range(len(data_f)):
        listt = []
        shop_id = data_f.iat[i, 0]
        province_id = str(data_f.iat[i, 1])
        spec_name = data_f.iat[i, 2]
        mileage = float(data_f.iat[i, 3])
        price = float(data_f.iat[i, 5])
        reg_date = data_f.iat[i, 4]
        spec_id = str(int(data_f.iat[i, 6]))
        car_age = data_f.iat[i, 7]
        sell_days = data_f.iat[i, 8]
        print("This car's info is :", car_age, mileage)

        low_age, up_age, low_mile, up_mile = 0, 0, 0, 0
        low_age, up_age, low_mile, up_mile = low_up(car_age, 1.5, mileage, 1.3)

        p = int(str(province_id[:2]))
        if p == 21:
            province = ('210000', '220000', '230000', '130000')
        elif p == 37:
            province = ('370000', '130000', '410000')
        elif p == 41:
            province = ('410000', '370000', '130000', '420000')
        elif p == 43:
            province = ('430000', '420000', '500000', '520000', '360000')
        elif p == 44:
            province = ('440000', '430000', '360000', '350000')
        elif p == 50:
            province = ('500000', '510000', '420000')
        else:
            province = ('210000', '410000', '440000')

        data = get_data(conn, spec_id, province)

        if data == [] or len(data) <= 1:
            print('Do not get any data to use, next one !!!')
            continue
        else:
            data_df = pd.DataFrame(data)
            # print(new_data_df1.loc[:, ('car_age','mileage','price')])
            new_data_df1 = data_df[(data_df['car_age'] >= low_age) & (data_df['car_age'] <= up_age) & (data_df['mileage'] >= low_mile) & (data_df['mileage'] <= up_mile)]
            # new_data_df2 = new_data_df1[(new_data_df1['mileage'] >= lower_mile) & (new_data_df1['mileage'] <= upper_mile)]
            if len(new_data_df1) >= 4:
                new_data_df2 = df_change(new_data_df1)
            else:
                continue
            if len(new_data_df2) >= 3:
                print('Now the effective num is :', kkk)
                min_price = round(min(new_data_df2['price']), 3)
                median_price = np.median(new_data_df2['price'])
                max_price = round(max(new_data_df2['price']), 3)
                advice_price = min_price + (median_price - min_price) * 0.75
                p_diff = round(price - advice_price,3)
                result_data = [shop_id, province_id, spec_name, mileage, reg_date, price, spec_id, car_age,sell_days, advice_price,p_diff]
                for j in result_data:
                    listt.append(str(j).strip('\n'))
                the_result.append(listt)
                kkk += 1
            else:
                continue
    conn.close()
    the_result = np.array(the_result)
    file = open(r'/Users/pujie/Desktop/selling_190527_result.csv', 'w', encoding="utf-8")
    np.savetxt(file, the_result, delimiter=',', fmt='%s')

    print('Success!!! The process running out!!!')
    print('total effective num is :', kkk)
