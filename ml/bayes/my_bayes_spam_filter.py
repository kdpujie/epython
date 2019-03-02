#encoding=utf-8
'''
Created on 2018年4月12日
@author: jie.pu
'''

import jieba
import os
import re


def test_nb():
    base_path = "/Users/pujie/workspace/python/xiaoxiang/ml/bayes/data"
    nb = NBSpamFilter(base_path + "/stop_words.txt")
    """训练集：normal邮件"""
    nb.add_norm_files(base_path + "/normal")
    """训练集：spam邮件"""
    nb.add_spam_files(base_path + "/spam")
    print("spam_file_number:", nb.spam_file_number)
    """测试集"""
    files = nb.get_files(base_path + "/test")
    result = {}
    for test_file in files:
        flag = nb.is_spam_bayes(base_path + "/test/" + test_file)
        result.setdefault(test_file, flag)
    """准确率"""
    right_count, error_count = 0, 0
    for name, category in result.items():
        print(name + ":", category)
        if (int(name) < 1000 and category is False) or (int(name) > 1000 and category is True):
            right_count += 1
        else:
            error_count += 1
    print("right_count=", right_count, "error_count=", error_count)
    print("正确率:", right_count/(right_count + error_count))


class NBSpamFilter(object):
    def __init__(self, stop_words_file):
        self.norm_file_number = 0
        self.spam_file_number = 0
        self.normDict = {}
        self.spamDict = {}
        self.stop_list = []
        """加载停用词"""
        for line in open(stop_words_file, encoding="GBK"):
            self.stop_list.append(line[:len(line) - 1])

    @staticmethod
    def get_files(file_path):
        file_names = os.listdir(file_path)
        return file_names

    """计算似然值"""
    @staticmethod
    def cal_likelihood(word_list, file_number, word_dict):
        likelihood = 1
        for word in word_list:
            if word in word_dict.keys():
                p = word_dict[word] / file_number
            else:
                p = 0.01
            likelihood *= p
        return likelihood

    """添加训练集中norm邮件内容"""
    def add_norm_files(self, norm_path):
        files = self.get_files(norm_path)
        self.norm_file_number = len(files)
        for fileName in files:
            self.cal_dict(norm_path + "/" + fileName, self.normDict)

    """添加训练集中的spam邮件内容"""
    def add_spam_files(self, spam_path):
        files = self.get_files(spam_path)
        self.spam_file_number = len(files)
        for fileName in files:
            self.cal_dict(spam_path + "/" + fileName, self.spamDict)

    """计算词频：若列表中的词已在词典中，则加1，否则添加进去"""
    def cal_dict(self, file, word_dict):
        for line in open(file, encoding="GBK"):
            """过滤掉非中文字符"""
            rule = re.compile(r"[^\u4e00-\u9fa5]")
            line = rule.sub("", line)
            """分词结果放入res_list"""
            res_list = list(jieba.cut(line))
            for word in res_list:
                if word not in self.stop_list and word.strip != '' and word != None:
                    if word in word_dict.keys():
                        word_dict[word] += 1
                    else:
                        word_dict.setdefault(word, 1)

    """给定一封邮件，判断是否是spam邮件"""
    def is_spam_bayes(self, test_file):
        word_list = []
        for line in open(test_file, encoding="GBK"):
            """过滤掉非中文字符"""
            rule = re.compile(r"[^\u4e00-\u9fa5]")
            line = rule.sub("", line)
            """分词结果放入res_list"""
            for word in jieba.cut(line):
                if word not in self.stop_list and word.strip != '' and word is not None:
                    if word not in word_list:
                        word_list.append(word)
        p_s_l = self.cal_likelihood(word_list, self.spam_file_number, self.spamDict)
        p_s = p_s_l * self.spam_file_number / (self.spam_file_number + self.norm_file_number)
        p_n_l = self.cal_likelihood(word_list, self.norm_file_number, self.normDict)
        p_n = p_n_l * self.norm_file_number / (self.spam_file_number + self.norm_file_number)
        return p_s > p_n


if __name__ == '__main__':
    test_nb()
