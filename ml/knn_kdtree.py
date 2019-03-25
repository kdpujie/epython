#encoding=utf-8
"""感知机算法的原始形式简单实现
Created on 2019年3月13日
@author: jie.pu"""

from numpy import *


class Node:
    """kd_tree数据节点"""
    def __init__(self, data, label, depth=0, lchild=None, rchild=None):
        self.data = data
        self.label = label
        self.depth = depth
        self.lchild = lchild
        self.rchild = rchild


class LargeHeap:

    def __init__(self):
        self.len = 0
        self.heap_list = []   # here we use a list to store heap

    def upward_adjust(self):
        # adjust to a large heap, assuming that only the last element in heaplist is not legal
        i = self.len - 1
        while i > 0:
            if self.heap_list[i][1] > self.heap_list[int((i - 1) / 2)][1]:
                self.heap_list[i], self.heap_list[int((i - 1) / 2)] = self.heap_list[int((i - 1) / 2)], self.heap_list[i]
                i = int((i - 1) / 2)
            else:
                break

    def add(self, x, distance):
        """
        :param x: type Node, indicates a sample
        :param distance: type double, use to indicate "large"
        :return: None
        """
        # add a point and adjust it to a large heap
        self.len += 1
        self.heap_list.append([x, distance])   # append it to the end, and use upward_adjust()
        self.upward_adjust()

    def downward_adjust(self):
        # adjust to a large heap, assuming that only the first element(top) in heap_list is not legal
        i = 0
        # attention to exchange with the large one of the children
        while (2*i + 1) < self.len:
            max_ind = 2*i +1
            if 2*i+2 < self.len and self.heap_list[(2*i + 1)][1] < self.heap_list[(2*i + 2)][1]:
                max_ind = 2*i + 2
            if self.heap_list[i][1] < self.heap_list[max_ind][1]:
                self.heap_list[i], self.heap_list[max_ind] = self.heap_list[max_ind], self.heap_list[i]
                i = max_ind
            else:
                break

    def pop(self):
        # pop the top of the heap
        if self.len == 1:
            self.heap_list = []
            self.len = 0
            return self.heap_list[0]
        # exchange for the last ele, and use downward_adjust()
        large = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        self.len -= 1
        self.heap_list = self.heap_list[:self.len]
        self.downward_adjust()
        return large


class KdTree(object):
    def __init__(self, dataset, label):
        self.kd_tree = None
        self.feature_number = 0
        self.nearest = None
        self.create(dataset, label)

    def create(self, dataset, label, depth=0):
        """
        递归创建kd tree
        :param dataset: 样本集
        :param label: 样本对应的分类
        :param depth: kd-tree当前的深度
        :return: 返回当前样本组成的tree node
        """
        if len(dataset) > 0:
            m, self.feature_number = shape(dataset)
            axis = depth % self.feature_number
            mid = int(m / 2)
            dataset_copy = sorted(dataset, key=lambda x:x[axis])
            node = Node(dataset_copy[mid], label[mid], depth)
            if depth == 0:
                self.kd_tree = node
            node.lchild = self.create(dataset_copy[:mid], label[:mid], depth + 1)
            node.rchild = self.create(dataset_copy[mid+1:], label[mid+1:], depth + 1)
            return node
        return None

    def _pre_order(self, node):
        """前序遍历查看kd tree的数据"""
        if node is not None:
            print(node.depth, node.data)
            self._pre_order(node.lchild)
            self._pre_order(node.rchild)

    def pre_order(self):
        self._pre_order(self.kd_tree)

    def search(self, x, count = 1):
        nearest = []
        for i in range(count):
            nearest.append([-1, None])
        # 初始化n个点，nearest是按照距离递减的方式
        self.nearest = np.array(nearest)

        def recurve(node):
            if node is not None:
                # 计算当前点的维度axis
                axis = node.depth % self.n
                # 计算测试点和当前点在axis维度上的差
                daxis = x[axis] - node.data[axis]
                # 如果小于进左子树，大于进右子树
                if daxis < 0:
                    recurve(node.lchild)
                else:
                    recurve(node.rchild)
                # 计算预测点x到当前点的距离dist
                dist = np.sqrt(np.sum(np.square(x - node.data)))
                for i, d in enumerate(self.nearest):
                    # 如果有比现在最近的n个点更近的点，更新最近的点
                    if d[0] < 0 or dist < d[0]:
                        # 插入第i个位置的点
                        self.nearest = np.insert(self.nearest, i, [dist, node], axis=0)
                        # 删除最后一个多出来的点
                        self.nearest = self.nearest[:-1]
                        break
                # 统计距离为-1的个数n
                n = list(self.nearest[:, 0]).count(-1)
                '''
                self.nearest[-n-1, 0]是当前nearest中已经有的最近点中，距离最大的点。
                self.nearest[-n-1, 0] > abs(daxis)代表以x为圆心，self.nearest[-n-1, 0]为半径的圆与axis
                相交，说明在左右子树里面有比self.nearest[-n-1, 0]更近的点
                '''
                if self.nearest[-n - 1, 0] > abs(daxis):
                    if daxis < 0:
                        recurve(node.rchild)
                    else:
                        recurve(node.lchild)


def simple_test():
    data = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    label = [0, 0, 0, 1, 1, 1]
    tree = KdTree(data, label)
    a = array([3,3])
    b = array([1,1])
    print(sqrt(sum(square(a - b))))


def test_large_heap():
    a = Node(1, 1)
    b = Node(2, 2)
    c = Node(3, 3)
    lh = LargeHeap()
    lh.add(a, 4)
    lh.add(b, 5)
    lh.add(c, 6)
    n = lh.pop()
    print(n[0].data, n[0].label)


if __name__ == '__main__':
    # simple_test()
    test_large_heap()
