from PIL import Image
import os
import os.path
import numpy as np
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import time

start = time.time()
n = 0
# 指明被遍历的文件夹
rootdir = r'F:\shujuji\HRSC2016-MS\AllImages'  # 图片路径
for parent, dirnames, filenames in os.walk(rootdir):
    # 遍历每一张图片
    for filename in filenames:
        currentPath = os.path.join(parent, filename)  # 目前图片的地址
        picture_number = filename[:-4]  # 图片去掉.png（.jpg）后的名字
        print("the picture name is:" + filename)
        txt_path = r'F:\shujuji\HRSC2016-MS\Annotations'  # 标签（xml或txt均可）文件存放的文件夹地址
        txt_file = os.listdir(txt_path)  # 将标签文件存放在txt_file列表里面
        if picture_number + '.xml' in txt_file:  # 如果图片有对应的标签文件则跳过
            pass
        else:
            print(currentPath)
            n += 1
            os.remove(currentPath)  # 没有对应的标签文件则删除
            end = time.time()
end = time.time()
print("Execution Time:", end - start)
print("删除的照片数为：", n)
