#!/usr/bin/env python
# -*- coding: utf-8 -*-
'引入模块，使用其提供的功能'

import time
import pymysql
import jieba

mysql_host = "10.4.8.2"
mysql_port = 20118
mysql_user = "tmp_admin"
mysql_pwd = "123@456"
mysql_db_name = "aps_test"


class Car(object):
    def __init__(self, host, port, user, password, db_name):
        self.stop_words = ["-", "款", "·", "—", "(", ")"]
        self.car_list = []
        self.current_date = time.strftime("%Y-%m-%d", time.localtime())
        # 打开数据库连接
        self.con = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name, charset="utf8")

    def save_car_segmentation(self, data):
        """保存"""
        sql = "insert into data_car_segmentation(master_brand_id, brand_id, serial_id, car_id, " \
              "master_brand_name, brand_name, serial_name, year, car_name, full_name, segmentation) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor = self.con.cursor()
            cursor.executemany(sql, data)
            self.con.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            cursor.close()

    def load_select_car(self):
        """加载select car"""
        sql = "select cm.MasterBrandId, br.BrandId,s.SerialId,ba.CarId, cm.Name,br.Name, s.Name, ba.Year, ba.Name, " \
              "concat(cm.Name,' ',br.Name,' ',s.Name,' ',ba.Year,' ',ba.Name)as full_name from car_basic ba, " \
              "car_serial s, car_brand br,car_masterbrand cm where ba.SerialId = s.SerialId and " \
              "s.BrandId = br.BrandId and br.MasterBrandId=cm.MasterBrandId and ba.IsEnabled is true"
        cursor = self.con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            c = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], self.cut(row[9]))
            self.car_list.append(c)
        cursor.close()

    def cut(self, sentence):
        words = set([])
        for word in jieba.cut(sentence):
            if word not in self.stop_words:
                words.add(word)
        return ' '.join(words).strip()

    def close(self):
        """关闭连接"""
        self.con.close()

    def get_car_size(self):
        """价值车型数量"""
        return len(self.car_list)


if __name__ == '__main__':
    c = Car(mysql_host, mysql_port, mysql_user, mysql_pwd, mysql_db_name)
    c.load_select_car()
    print("加载车型数：%d" % c.get_car_size())
    c.save_car_segmentation(c.car_list)
    c.close()
