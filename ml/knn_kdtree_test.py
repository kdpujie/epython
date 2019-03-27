#encoding=utf-8
"""kd_tree实现
Created on 2019年3月27日
@author: jie.pu"""

import pandas
from ml import knn_kdtree
from pandas import DataFrame


def read_data(file):
    """vehicle_id, brand_id, brand_name, series_id, series_name, spec_id, spec_name, current_price, mileage,
    region_code, region"""
    df = pandas.read_csv(file)
    data = []
    label = []
    for line in df.values:
        x = [line[1], line[3], line[4], line[7], line[8], line[11], line[12]]
        y = line[3]
        data.append(x)
        label.append(y)

    return data, label


def knn_test(data, label):
    tree = knn_kdtree.KdTree(data, label)
    k_list = tree.k_nearest_neighbor(5, [1765, 6.9, 2014, 6.0, 6.74, 13.88, 105310])
    for el in k_list:
        print(el[0].data, el[0].label, el[1])


if __name__ == '__main__':
    data, label = read_data("/Users/pujie/workspace/python/exercise/ml/data/guazi_vehicle.csv")
    knn_test(data, label)
