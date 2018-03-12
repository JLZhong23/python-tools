# -*- coding:utf-8 -*-
'''
    本模块提供与字典相关的操作
'''
import re
import os
import sys
import csv
import xlrd
import codecs
import random
import chardet
import numpy as np
from copy import deepcopy
try:
    import cPickle as pickle
except:
    import pickle


def find_max_n_in_dict(ori_dict, N):
    '''
        本函数用于在字典中选取最大的N个
        [ori_dict](dict): 原字典
        [N](int): 最大的个数
    '''
    i = 0
    new_dict = {}
    ori_dict = dict(ori_dict)
    for i in range(0,N):
        max_key = max(ori_dict, key=lambda x: ori_dict[x])
        new_dict[max_key] = ori_dict.pop(max_key)
    return new_dict
def find_min_n_in_dict(ori_dict, N):
    '''
        本函数用于在字典中选取最小的N个
        [ori_dict](dict): 原字典
        [N](int): 最小的个数
    '''
    i = 0
    new_dict = {}
    ori_dict = dict(ori_dict)
    for i in range(0,N):
        min_key = min(ori_dict, key=lambda x: ori_dict[x])
        new_dict[min_key] = ori_dict.pop(min_key)
    return new_dict


def list_to_dict(ori_list, key_place=0):
    '''
        本函数用于将二级列表以其最低级列表的指定位置为键，其他位置为值生成字典
        [ori_list](list): 输入列表
        [key_place](int): 作为键的位置
    '''
    tar_dict = {}
    for line in ori_list:
        tar_dict[line[key_place]] = [element for element in (line[:key_place]+line[key_place+1:])]
    return tar_dict

