'''
    本模块提供各种易于使用的图形绘制函数
    注意：此模块必须安装字体SimHei才能正常显示中文，若中文乱码，双击运行字体文件simhei.ttf即可安装字体并正常使用，字体文件simhei.tff已置于工具集根目录中
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
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.font_manager import _rebuild
from palettable.colorbrewer.qualitative import Dark2_7
#from markdown2pdf import convert_md_2_pdf as markdown2pdf
_rebuild()
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def draw_pie(title, labels, sizes, explode=None, output_path='./a.jpg', shadow=False, show_result=True):
    '''
        本函数用于绘制饼图
        [labels](list): 标签列表
        [sizes](list): 每个标签所对应的大小所组成的列表，与标签列表对应位置元素相对应（无需提供相对大小）
        [explode](tuple): 强调块元组，被强调的元素对应的位置为非零值（建议为0.05），其他元素对应位置为0，无需强调时不传入此参数
        [output_path](str): 输出的文件路径（含文件名）
        [shadow](bool): 是否有阴影（默认为无）(阴影真的很难看)
        [show_result](bool): 是否产生直接输出（默认为是）
    '''
    if explode:
        if not (len(labels) == len(sizes)) and (len(sizes) == len(explode)):
            raise("Error: labels, sizes, explode must be of the same size")
    else:
        if not (len(labels) == len(sizes)):
            raise("Error: labels and sizes must be of the same size")
    #用来正常显示中文标签
    proptease = fm.FontProperties()
    proptease.set_size(size=13)
    #调节图形大小，宽，高
    fig = plt.figure(figsize=(9,9),dpi=400)
    ax  = fig.add_subplot(111)
    ax.set_position([0.1,0.1,0.6,0.85])
    #定义饼状图的标签，标签是列表
    # labels = [name for name in people.keys()]
    #每个标签占多大，会自动去算百分比
    # sizes = [people[name]['time'] for name in people.keys()]
    #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.05,0,0)
    # cmap=plt.get_cmap('Pastel1')

    colors = cm.Set3(X=range(len(labels)),alpha=0.7)
    patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = shadow,
                                    startangle = 90,pctdistance = 0.6)

    #labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    #autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    #shadow，饼是否有阴影
    #startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    #pctdistance，百分比的text离圆心的距离
    #patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend(bbox_to_anchor=(1.32,0.2), loc="lower right")
    plt.title(title, fontsize=20, fontproperties=proptease)
    if output_path:
        plt.savefig(output_path)
    if show_result:
        plt.show()


def draw_bar(title, labels, first_sizes, other_sizes=[], sub_labels=[], output_path='', show_result=True, y_value=True):
    '''
        本函数用于绘制柱状图
        [title](str): 图标题
        [labels](list): X轴主标签列表
        [first_sizes](list): 每个主标签的第一个子标签的值组成的列表(不可缺省)
        [other_sizes](list[list]): 每个主标签的所有其他子标签的值组成的列表（列表的列表）(就算忘了变成列表的列表也不会出bug）（缺省则只画一个子标签）
        [sub_labels](list): 子标签列表
        [output_path](str): 输出的文件路径（含文件名）
        [show_result](bool): 是否产生直接输出（默认为是）
        [y_value](bool): 是否显示y值（默认为是）
    '''
    if other_sizes:
        if type(other_sizes[0]) != type([]):
            other_sizes = [other_sizes]
    fig = plt.figure(figsize=(9,6),dpi=400)
    ax  = fig.add_subplot(111)
    n = len(labels)
    if len(other_sizes) >=2:
        div_size = int(len(other_sizes)/1.5)     
        X = np.arange(n*div_size,step=div_size)+1
    else:
        div_size = 1
        X = np.arange(n)+1
    # print(X)
    #X是1,2,3,4,5,6,7,8,柱的个数
    # numpy.random.uniform(low=0.0, high=1.0, size=None), normal
    #uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
    #用来正常显示中文标签
    proptease = fm.FontProperties()
    proptease.set_size(size=13)
    plt.title(title, fontsize=20, fontproperties=proptease)  
    # plt.box(on=None)
    ax.spines['top'].set_visible(False)  
    ax.spines['right'].set_visible(False)  
    ax.spines['bottom'].set_visible(True)  
    ax.spines['left'].set_visible(False)  
    ax.yaxis.grid()
    ax.yaxis.set_ticks([])
    # ax.yaxis.grid()
    # axes.set_yticks([])
    colors = cm.Set3(X=range(len(other_sizes)+1),alpha=0.7)
    #print(first_sizes)
    if len(other_sizes) <= 1:
        p1 = plt.bar(X,first_sizes,width = 0.35,facecolor = colors[0], edgecolor = 'white',tick_label = labels)
        tickle_label_place = 0
    else:
        p1 = plt.bar(X,first_sizes,width = 0.35,facecolor = colors[0], edgecolor = 'white')
        tickle_label_place = int(len(other_sizes)/2)
    if y_value:
        for a,b in zip(X,first_sizes):    
            plt.text(a, b+0.1, '%.0f' % b, ha='center', va= 'bottom',fontsize=11/div_size)        
    p = []
    #width:柱的宽度
    i = 1
    for sizes in other_sizes:
        if i == tickle_label_place:
            p.append(plt.bar(X+0.35*i,sizes,width = 0.35,facecolor = colors[i],edgecolor = 'white',tick_label = labels))
            print(1)
        else:
            p.append(plt.bar(X+0.35*i,sizes,width = 0.35,facecolor = colors[i],edgecolor = 'white'))
        if y_value:
            for a,b in zip(X+0.35*i,sizes):
                plt.text(a, b+0.1, '%.0f' % b, ha='center', va= 'bottom',fontsize=11/div_size) 
        i+=1
    if sub_labels:
        plt.legend([p1]+p, labels=sub_labels, bbox_to_anchor=(1.15,1.2), loc="upper right")
    #水平柱状图plt.barh，属性中宽度width变成了高度height
    #打两组数据时用+
    #facecolor柱状图里填充的颜色
    #edgecolor是边框的颜色
    #想把一组数据打到下边，在数据前使用负号
    #plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
    #给图加text
    n=0
    # plt.bar(x, num_list1, width=width, label='girl',tick_label = name_list,fc = 'r')
    if output_path:
        plt.savefig(output_path)
    if show_result:
        plt.show()