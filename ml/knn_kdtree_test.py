#encoding=utf-8
"""kd_tree实现
Created on 2019年3月27日
@author: jie.pu"""

import pandas
from ml import knn_kdtree
from pandas import DataFrame


def read_data(file):
    """
    car_id, "brand_id", "series_id","spec_id", "guide_price", "car_year"  , "car_age", "mileage" , "city_id", "sale_price",
    "brand_name", "series_name", "spec_name"
    """
    df = pandas.read_csv(file)
    data = []
    label = []
    for line in df.values:
        x = [line[3], line[4], line[5], line[6], line[7], line[9]]
        y = line[9]
        data.append(x)
        label.append(y)

    return data, label


def knn_test(data, label):
    tree = knn_kdtree.KdTree(data, label)
    k_list = tree.k_nearest_neighbor(10, [16270, 13.09, 2012, 4, 3.67, 8.424])
    for el in k_list:
        print(el[0].data, el[1])


if __name__ == '__main__':
    data, label = read_data("/Users/pujie/workspace/python/exercise/ml/data/guazi_vehicle.csv")
    knn_test(data, label)
