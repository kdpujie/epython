#encoding=utf-8
'''
感知机算法的原始形式简单实现
Created on 2019年3月2日
@author: jie.pu
'''

import pandas
from ml import perceptron
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler


def read_data(file):
    y, test_y = [], []
    x, test_x = [], []
    df = pandas.read_csv(file)
#    print(df)
    index = 0
    for line in df.values:
        x0 = [line[1], line[2], line[3], line[4], line[5]]
        y0 = line[0]
        if y0 < 1 :
            y0 = -1
        if index > 2999:
            y.append(y0)
            x.append(x0)
        else:
            test_y.append(y0)
            test_x.append(x0)
        index += 1
    ss = StandardScaler()
    std_x = ss.fit_transform(x)
    std_test_x = ss.fit_transform(test_x)
    std_x = DataFrame(std_x)
    std_test_x = DataFrame(std_test_x)
    std_x.columns = ['selling_price', 'age', 'sell_speed', 'mileage', 'avg_mileage']
    std_test_x.columns = ['selling_price', 'age', 'sell_speed', 'mileage', 'avg_mileage']
    return std_x.values, y, std_test_x.values, test_y


def train(train_file):
    x, y, test_x, test_y = read_data(train_file)
    clf = perceptron.Perceptron(1, 100)
    clf.fit(x, y)
    clf.test(test_x, test_y)


if __name__ == '__main__':
    train("/Users/pujie/workspace/python/exercise/ml/data/perceptron_train.csv")