#encoding=utf-8
"""
决策树的ID3算法
Created on 2019年6月06日
@author: jie.pu
"""
import numpy as np
import pandas as pd


class Node(object):
    def __init__(self, value=None, feature=None, y=None, data=None):
        self.splitting_feature = feature   #子节点分类依据的特征，最优特征
        self.splitting_point = value  # 最优切分点
        self.children = []      # child:子节点
        self.y = y           # y:类标记（叶节点才有）
        self.data = data     # data:包含数据（叶节点才有）

    def append(self, node):  # 添加子节点
        self.children.append(node)

    def predict(self, features):  # 预测数据所述类
        if self.y is not None:
            return self.y
        for c in self.children:
            if c.x == features[self.splitting_feature]:
                return c.predict(features)


class DTreeID3(object):
    def __init__(self, epsilon=0, alpha=0):
        """信息增益阈值"""
        self.epsilon = epsilon
        self.alpha = alpha
        self.tree = Node()

    def prob(self, datasets):
        """极大似然估计求概率"""
        size = len(datasets)
        labels = set(datasets)
        p = {l: 0 for l in labels}
        for d in datasets:
            p[d] += 1
        for i in p.items():
            p[i[0]] /= size
        return p

    def entropy(self, datasets):
        """求集合D的熵H(D)"""
        p = self.prob(datasets)
        value = list(p.values())
        return -np.sum(np.multiply(value, np.log2(value)))

    def conditional_entropy(self, datasets, feature_index):
        """求条件熵H(D|A)"""
        feature_values_range = set(datasets.iloc[feature_index])
        p = {x: [] for x in feature_values_range}
        """最后一行为类别"""
        for index, c in enumerate(datasets.iloc[-1]):
            p[datasets.iloc[feature_index][index]].append(c)
        return sum([self.prob(datasets.iloc[feature_index])[f_value] * self.entropy(p[f_value]) for f_value in p.keys()])

    def information_gain(self, datasets):
        """求最大信息增益 H(D) - H(D|A)"""
        datasets = datasets.T
        H_D = self.entropy(datasets.iloc[-1])
        max_ig, feature_index = 0, 0
        for i in range(len(datasets) - 1):
            H_D_A = self.conditional_entropy(datasets, i)
            if (H_D - H_D_A) > max_ig:
                max_ig = H_D - H_D_A
                feature_index = i
        return feature_index, max_ig

    def fit(self, datasets):
        """训练数据"""
        self.create_tree(datasets, self.tree)

    def create_tree(self, datasets, node):
        label_name = datasets.columns[-1]
        """判断样本是否为同一类输出Di，如果是则返回单节点树T。标记类别为Di"""
        if len(datasets[label_name].value_counts()) == 1:
            node.data = datasets[label_name]
            node.y = datasets[label_name][0]
            return
        """判断特征是否为空，如果是则返回单节点树T，标记类别为样本中输出类别D实例数最多的类别"""
        if len(datasets.columns[:-1]) == 0:
            node.data = datasets[label_name]
            node.y = datasets[label_name].value_counts().index[0]
            return
        """计算A中的各个特征（一共n个）对输出D的信息增益，选择信息增益最大的特征Ag。"""
        feature_index, max_ig = self.information_gain(datasets)
        """如果Ag的信息增益小于阈值ε，则返回单节点树T，标记类别为样本中输出类别D实例数最多的类别。"""
        if max_ig <= self.epsilon:
            node.data = datasets[label_name]
            node.y = datasets[label_name].value_counts().index[0]
            return
        """按特征Ag的不同取值Agi将对应的样本输出D分成不同的类别Di。每个类别产生一个子节点。对应特征值为Agi。返回增加了节点的数T。"""
        vc = datasets[datasets.columns[feature_index]].value_counts()
        for c in vc.index:
            node.best_feature = feature_index
            child = Node(c)
            node.append(child)
            sub_dataset = pd.DataFrame([list(i) for i in datasets.values if i[feature_index] == c], columns=datasets.columns)
            self.create_tree(sub_dataset, child)


def print_node(node, depth=0):  # 打印树所有节点
    if node.best_feature is None:
        print(depth, (node.best_feature, node.splitting_point, node.y, len(node.data)))
    else:
        print(depth, (node.best_feature, node.splitting_point))
        for c in node.children:
            print_node(c, depth+1)


if __name__ == "__main__":
    datasets = np.array([
                   ['青年', '否', '否', '一般', '否'],
                   ['青年', '否', '否', '好', '否'],
                   ['青年', '是', '否', '好', '是'],
                   ['青年', '是', '是', '一般', '是'],
                   ['青年', '否', '否', '一般', '否'],
                   ['中年', '否', '否', '一般', '否'],
                   ['中年', '否', '否', '好', '否'],
                   ['中年', '是', '是', '好', '是'],
                   ['中年', '否', '是', '非常好', '是'],
                   ['中年', '否', '是', '非常好', '是'],
                   ['老年', '否', '是', '非常好', '是'],
                   ['老年', '否', '是', '好', '是'],
                   ['老年', '是', '否', '好', '是'],
                   ['老年', '是', '否', '非常好', '是'],
                   ['老年', '否', '否', '一般', '否']])
                  # ['青年', '否', '否', '一般', '是']])  # 在李航原始数据上多加了最后这行数据，以便体现剪枝效果

    datalabels = np.array(['年龄', '有工作', '有自己的房子', '信贷情况', '类别'])
    train_data = pd.DataFrame(datasets, columns=datalabels)
    test_data = ['老年', '否', '否', '一般']

    dt = DTreeID3(epsilon=0)  # 可修改epsilon查看预剪枝效果
    dt.fit(train_data)
    print_node(dt.tree)