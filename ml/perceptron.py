#encoding=utf-8
'''
感知机算法的原始形式简单实现
Created on 2019年3月2日
@author: jie.pu
'''

import numpy as np
import sys


# 折页损失函数
class Hinge(object):
    def __init__(self, threshold=0):
        self.threshold = threshold

    def loss(self, p, y):
#       z = p * y
#       if z <= self.threshold:
#          return self.threshold - z
        if p * y > 0:
            return 0
        return 1


class Perceptron(object):
    def __init__(self, eta=1, max_iter=10):
        self.eta = eta
        self.intercept = 0
        self.max_iter = max_iter
        self.w = []
        self.loss = Hinge()

    def fit(self, x=[], y=[]):
        x = np.mat(x)
        self._plain_sgd(x, y)
        return self

    def _plain_sgd(self, x, y):
        w = np.zeros((1, len(x.T)), float)                          # 矩阵计算为行*列，所以w的列数 = x的行数
        b = self.intercept
        min_sum_loss = sys.maxsize
        for epoch in range(self.max_iter):
            sum_loss = 0
            for i in range(len(x)):
                p = np.dot(x[i], w.T) + b                             # 计算w*x +b
                update = self.loss.loss(p, y[i])                    # 误分类点的损失非0
                if update != 0:
                    sum_loss += 1
                    w += self.eta * y[i] * x[i]                     # 调整w，使超平面向i点移动
                    b += self.eta * y[i]                            # 调整b，使超平面向i点移动
            print("--%d Epoch, sum_loss=%d, min=%d, w=%s, opt_w=%s, b=%d, opt_intercept=%d" %
                  (epoch + 1, sum_loss, min_sum_loss, w, self.w, b, self.intercept))
            if sum_loss < min_sum_loss:                             # 记录迭代中最优的w、b
                min_sum_loss = sum_loss
                self.w = w + np.zeros((1, len(w)), float)
                self.intercept = b
            if sum_loss == 0:                                       # 无误分类点，则退出迭代
                break

    def test(self, test_x, test_y):
        size = len(test_x)
        failed_count = 0
        if size < 0:
            pass
        for i in range(len(test_x)):
            print(test_x[i], self.w.T)
            p = np.dot(test_x[i], self.w.T) + self.intercept
            r = self.loss.loss(p, test_y[i])
            if r != 0:
                failed_count += 1
        success_rate = (1.0 - (float(failed_count) / size)) * 100
        print("success rate:", success_rate, "%")
        print("All input: ", size, " failed_count: ", failed_count)


if __name__ == '__main__':
    x = [[4, 3], [3, 3], [1, 1]]
    y = [1, 1, -1]
    clf = Perceptron()
    clf.fit(x, y)
