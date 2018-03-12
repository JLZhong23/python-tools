# -*- coding:utf-8 -*-
'''
    本模块提供与随机选取相关的函数
'''
import re
import os
import sys
import csv
import xlrd
import time
import codecs
import random
import chardet
import numpy as np
from copy import deepcopy
try:
    import cPickle as pickle
except:
    import pickle


def seed_random(seed,where):
    '''
        本函数用于在指定范围内利用指定种子生成一个随机整数
        [seed](int): 生成随机数的种子
        [where](list): 第一个元素为起始位置，第二个元素为结束位置
    '''
    random.seed(seed)
    return random.randrange(where[0],where[1])


def random_choose(ori_list, num, seed=1000, sort = True, split = False):
    '''
        本函数用于从一个序列中随机选取数个元素，对于有序序列可保留原顺序
        [ori_list](list/set/..): 原序列
        [num](int): 选取的个数
        [seed](可选用不同种子)
        [sort](bool): 是否保留原顺序（默认为是）（需提高效率时可设置为False）
        [split](bool): 是否同时返回新列表与选择完毕后剩下的列表（缺省为否）（非常有用）
    '''
    new_list = []
    if type(ori_list) != type(new_list):
        ori_list = list(ori_list)
    pipe_list = list(ori_list)
    length = len(ori_list)
    i = 0
    while i < num:
        index = seed_random(seed, [0, length-1])
        new_list.append(pipe_list.pop(index))
        i+=1
        length -= 1
        # if not i%10000:
        #     print(str(int(i/10000))+' choosen')
    if sort:
        new_list.sort(key=ori_list.index)
        if split:
            pipe_list.sort(key=ori_list.index)
    if split:
        return new_list, pipe_list
    else:
        return new_list

