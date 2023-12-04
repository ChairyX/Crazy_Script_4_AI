# 将UCAS_AOD格式转为DOTA
import os
import random
import numpy as np
from numpy import *

txt_filepath = r" 路径 "  # 原始txt文件所存文件夹，文件夹可以有一个或多个txt文件
save_filepath = r" 路径 "  # 更改后txt文件存放的文件夹

total_txt = os.listdir(txt_filepath)  # 返回指定的文件夹包含的文件或文件夹的名字的列表
num = len(total_txt)
txt_list = range(num)  # 创建从0到num的整数列表
files = os.listdir(save_filepath)

for i in txt_list:  # 遍历每一个文件

    name = total_txt[i]
    readfile = open(txt_filepath + "\\" + name, 'r')  # 读取文件
    f_line = readfile.readlines()  # 读取txt文件中每一行
    print(len(f_line))

    for j in range(len(f_line)):
        line_list = f_line[j].strip().split('\t')
        x1 = int(eval(line_list[0]))
        y1 = int(eval(line_list[1]))
        x2 = int(eval(line_list[2]))
        y2 = int(eval(line_list[3]))
        x3 = int(eval(line_list[4]))
        y3 = int(eval(line_list[5]))
        x4 = int(eval(line_list[6]))
        y4 = int(eval(line_list[7]))

        save_txt = open(save_filepath + "\\" + name, 'a')

        save_txt.write(
            "{} {} {} {} {} {} {} {} {} {}\n".format(float(x1), float(y1), float(x2),
                                                     float(y2), float(x3), float(y3),
                                                     float(x4), float(y4),
                                                     'plane', 0))
