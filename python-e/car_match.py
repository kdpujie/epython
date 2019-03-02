#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""引入模块，使用其提供的功能"""

__author__ = 'pujie'

import jieba
import pymysql
import time
import datetime

mysql_host = "10.4.8.2"
mysql_port = 20118
mysql_user = "tmp_admin"
mysql_pwd = "123@456"
mysql_db_name = "aps_test"


class CarBasic(object):
    """rank, city_id, brand_id,series_id, brand_name, series_name"""
    def __init__(self, rank, city_id, brand_id, series_id, car_id, brand_name, series_name, car_name, score, median_price):
        self.rank = rank
        self.city_id = city_id
        self.brand_id = brand_id
        self.series_id = series_id
        self.car_id = car_id
        self.brand_name = brand_name
        self.series_name = series_name
        self.car_name= car_name
        self.score = score
        self.median_price = median_price


class Vehicle(object):
    """r.region_code, province, car_type, mileage, first_place_time, url"""
    def __init__(self, region_code, province, car_type, mileage, first_place_time, url, vehicle_id):
        self.city_id = region_code
        self.city_name = province
        self.tile = car_type
        self.mileage = mileage
        self.first_register_date = first_place_time
        self.url = url
        self.vehicle_id = vehicle_id


class DbOperator(object):

    def __init__(self, host, port, user, password, db_name):
        self.car_list = []
        self.current_date = time.strftime("%Y-%m-%d", time.localtime())
        # 打开数据库连接
        self.con = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name, charset="utf8")

    def get_car_size(self):
        """价值车型数量"""
        return len(self.car_list)

    def save_car(self, rank, city_id, brand_id, brand_name, series_id, series_name):
        """价值车型入库"""
        sql = "insert into data_select_car(rank, city_id, brand_id, brand_name, series_id, series_name, p_date) " \
              "values(%s,%s,%s,%s,%s,%s,%s)"
        data =[(rank, city_id, brand_id, brand_name, series_id, series_name, self.current_date)]
        cursor = self.con.cursor()
        cursor.executemany(sql, data)
        self.con.commit()
        cursor.close()

    def load_select_car(self):
        """加载select car"""
        sql = "select `rank`, city_id, brand_id,series_id,c.CarId, brand_name, series_name, c.Name, " \
              "score, median_price from data_select_car s join car_basic c on s.series_id = c.SerialId " \
              "and s.p_date = '2019-01-08'"
        cursor = self.con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            c = CarBasic(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            self.car_list.append(c)
        cursor.close()

    def save_vehicle(self, data):
        """筛选出来的天天拍车车源入库"""
        sql = "insert into data_purchase_vehicle(city_id, `rank`, brand_id, series_id, brand_name, " \
              "series_name, source, mileage, vehicle_title, vehicle_url, publish_date, city_name, " \
              "first_register_date,vehicle_id,median_price,score,car_age,car_id,car_name) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor = self.con.cursor()
            cursor.executemany(sql, data)
            self.con.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            cursor.close()

    def auction_vehicle_match(self):
        """匹配并入库"""
        sql = "select r.region_code, province, car_type, mileage,first_place_time,url,c.id from crawl_online_auction " \
              "c, sys_region r where c.province = r.name and DATE_FORMAT(created_date,'%Y-%m-%d') = '2019-01-03'"
        cursor = self.con.cursor()
        cursor.execute(sql)
        vs = []
        for vehicle in cursor.fetchall():
            v = Vehicle(vehicle[0], vehicle[1], vehicle[2], int(vehicle[3]), vehicle[4], vehicle[5], vehicle[6])
            flag = False
            for car in self.car_list:
                words = list(jieba.cut(car.brand_name))
                for word in words:
                    # 包含车型和车系 则会匹配成功
                    if (word not in "-") and (word in v.tile) and (car.series_name in v.tile):
                        flag = True
                        break
                if flag:
                    break
            if flag and self.is_exist_vehicle(v.vehicle_id) is not True:
                start = datetime.datetime.strptime(v.first_register_date, "%Y-%m")
                now = datetime.datetime.now()
                car_age = now.year - start.year
                c = (v.city_id, car.rank, car.brand_id, car.series_id, car.brand_name, car.series_name, 1,
                     v.mileage, v.tile, v.url, self.current_date, v.city_name, v.first_register_date,v.vehicle_id,
                     car.median_price, car.score, car_age, car.car_id, car.car_name)
                vs.append(c)
        self.save_vehicle(vs)
        self.con.commit()
        cursor.close()

    def is_exist_vehicle(self, vehicle_id):
        """车源是否存在"""
        sql = "select count(*) from data_purchase_vehicle where vehicle_id = %s"
        cursor = self.con.cursor()
        cursor.execute(sql, vehicle_id)
        data = cursor.fetchone()
        return data[0] > 0

    def close(self):
        """关闭连接"""
        self.con.close()


if __name__ == '__main__':
    db = DbOperator(mysql_host, mysql_port, mysql_user, mysql_pwd, mysql_db_name)
    db.load_select_car()
    print("加载车型数：%d" % db.get_car_size())
    db.auction_vehicle_match()
    db.close()