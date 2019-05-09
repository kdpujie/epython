#encoding=utf-8
"""
感知机算法的原始形式简单实现
Created on 2019年3月2日
@author: jie.pu
"""

import numpy as np
from ml.sgd_fast import plain_sgd, Hinge


class PerceptronV2(object):
    def __init__(self, eta=1, max_iter=10):
        self.eta = eta
        self.intercept = 0
        self.max_iter = max_iter
        self.w = []
        self.loss = Hinge()

    def fit(self, x=[], y=[]):
        x = np.mat(x)
        w = np.zeros((1, len(x.T)), float)
        self.w, self.intercept = plain_sgd(w, self.intercept, self.loss, x, y)
        return self

    def test(self, test_x, test_y):
        size = len(test_x)
        tp_count = 0
        fn_count = 0
        fp_count = 0
        tn_count = 0
        if size < 0:
            pass
        for i in range(len(test_x)):
            # print(test_x[i], self.w.T)
            p = np.dot(test_x[i], self.w.T) + self.intercept
            if test_y[i] > 0:
                if p > 0:
                    tp_count += 1
                else:
                    fn_count += 1
            else:
                if p > 0:
                    fp_count += 1
                else:
                    tn_count += 1
        print("TP=", tp_count, ", fn=", fn_count, ", fp=", fp_count, ", tn=", tn_count)
        print("precision: ", tp_count / (tp_count + fp_count), " recall: ", tp_count / (tp_count + fn_count))
        print("accuracy:", (tp_count + tn_count) / size)


if __name__ == '__main__':
    x = [[4, 3], [3, 3], [1, 1]]
    y = [1, 1, -1]
    clf = PerceptronV2()
    clf.fit(x, y)
