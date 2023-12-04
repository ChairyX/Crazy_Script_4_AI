# 统计类别数量
import os
import random
import numpy as np
from numpy import *

txt_filepath = r"----"  # 原始txt文件所存文件夹，文件夹可以有一个或多个txt文件

total_txt = os.listdir(txt_filepath)  # 返回指定的文件夹包含的文件或文件夹的名字的列表
num = len(total_txt)
txt_list = range(num)  # 创建从0到num的整数列表
plane_num = 0
vehicle_num = 0
ship_num = 0
for i in txt_list:  # 遍历每一个文件

    name = total_txt[i]
    readfile = open(txt_filepath + "\\" + name, 'r')  # 读取文件
    f_line = readfile.readlines()  # 读取txt文件中每一行

    for j in range(len(f_line)):
        line_list = f_line[j].strip().split(' ')
        class_name = line_list[8]
        if class_name == 'plane':
            plane_num += 1
        if class_name == 'vehicle':
            vehicle_num += 1
        if class_name == 'ship':
            ship_num += 1
print('飞机的instance为：{}，车的instance为：{}，船的instance为：{}'.format(plane_num, vehicle_num, ship_num))