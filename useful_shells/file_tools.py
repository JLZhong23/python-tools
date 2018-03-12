# -*- coding:utf-8 -*-
'''
    本模块提供与文件读写相关的操作
'''
import re
import os
import sys
import csv
import codecs
import xlrd
try:
    import cPickle as pickle
except:
    import pickle


def read_xlsx(filepath):
    '''
        本函数用于将excel文件以多级列表形式读取

        还没测试是否可用

        [filepath](str): 文件目录（含文件名）
    '''
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    content = list(table.row_values)
    if data:
        data.release_resources()
        del data
    return content

def read_txt_as_csv(filepath, divider=','):
    '''
        本函数用于将以其他符号作为分隔符的文件读取为多级列表的形式
        [filepath](str): 文件目录（含文件名）
        [divider](str): 分隔符（缺省为英文逗号）
    '''
    file = open(filepath,'r', encoding='utf-8')
    content = file.readlines()
    result = [line.strip().split(divider) for line in content]
    if file:
        file.close
    return result


def html_killer(input_string):
    '''
        本函数返回输入字符串去除了所有html标签及特殊符号（如&nbsp;)后的剩余部分
        [input_string](str): 待处理字符串
    '''
    result_string = re.sub(r'<[^<>]*>|&[^&;]*;','',input_string).strip()
    return result_string


def simbol_killer(input_string):
    '''
        本函数返回输入字符串去除了各种语言字符后的剩余部分
        [input_string](str): 待处理字符串
    '''
    new_string = re.sub(r'[\_\=\+\(\)》《\?\？\\\/【】\！!@#￥%…&（）/，、。+~\!\n\t \,\'\"“”‘’]|\^[^\^;]*;',' ',input_string).strip()
    new_string = re.sub(r' +',' ',new_string)
    return new_string


def num_killer(input_string):
    '''
        本函数返回输入字符串去除了所有数字后的剩余部分
        [input_string](str): 待处理字符串
    '''
    new_string = re.sub(r'[0-9]*',' ',input_string).strip()
    new_string = re.sub(r' +',' ',new_string)
    return new_string


def load_data(dump_path='', dump_filename=''):
    '''
        本函数通过提供文件路径直接读取通过pickle储存的文件

    '''
    dump_filepath = dump_path+dump_filename
    with open(dump_filepath, 'rb') as dump_file:
        data = pickle.load(dump_file)
    return data


def unix2dos(r_filename, w_filename):
    '''
        本函数将unix格式文件（输入）转换为dos文件格式（输出）
        [r_filename](str): 输入文件路径
        [w_filename](str): 输出文件路径
    '''
    with open(r_filename, 'r') as f:
        data = f.read()
        data_new = data.replace('\n', '\r\n')
    with open(w_filename, 'w') as f1:
        f1.write(data_new)


def dos2unix(r_filename, w_filename):
    '''
        本函数将dos格式文件（输入）转换为unix文件格式（输出）
        [r_filename](str): 输入文件路径
        [w_filename](str): 输出文件路径
    '''
    with open(r_filename, 'r') as f:
        data = f.read()
        data_new = data.replace('\r\n', '\n')
    with open(w_filename, 'w') as f1:
        f1.write(data_new)

