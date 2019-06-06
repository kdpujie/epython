#encoding=utf-8
"""
感知机算法的原始形式简单实现
Created on 2019年5月9日
@author: jie.pu
"""

import numpy as np


# 折页损失函数
class Hinge(object):
    """Hinge loss for binary classification tasks with y in {-1,1}
    """
    def __init__(self, threshold=0):
        self.threshold = threshold

    def loss(self, p, y):
        z = p * y
        if z <= self.threshold:
            return self.threshold - z
        return 0.0

    def _dloss(self, p, y):
        z = p * y
        if z <= self.threshold:
            return -y
        return 0.0


def plain_sgd(weights, intercept, loss, x, y, max_iter=100, eta0=1, n_iter_no_change=5):
    update = 0.0
    best_loss = np.inf
    no_improvement_count = 0
    for epoch in range(max_iter):
        sum_loss = 0
        for i in range(len(x)):
            p = np.dot(x[i], weights.T) + intercept   # 计算w*x +b
            sum_loss += loss.loss(p, y[i])          # 误分类点的损失非0
            dloss = loss._dloss(p, y[i])
            update = -eta0 * dloss
            if update != 0:
                weights += update * x[i]            # 调整w，使超平面向i点移动
                intercept += update                 # 调整b，使超平面向i点移动
        print("--%d Epoch, w=%s, b=%d, Avg.loss: %f" % (epoch + 1, weights, intercept, sum_loss / len(x)))
        if sum_loss >= best_loss:
            no_improvement_count += 1
        else:
            no_improvement_count = 0
        if sum_loss < best_loss:
            best_loss = sum_loss
        if no_improvement_count > n_iter_no_change:
            break
    return weights, intercept

