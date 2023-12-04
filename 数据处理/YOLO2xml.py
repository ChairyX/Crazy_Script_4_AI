# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image

###将txt格式文件转换为xml格式文件
# 图像存储位置
src_img_dir = "F:\LEVIR\JPEGImages"
# 图像的 ground truth 的 txt 文件存放位置
# windows 系统路径用“\”,ubuntu 中用“/”
src_txt_dir = "F:\\LEVIR\\Annotations\\"
src_xml_dir = "F:\\LEVIR\\anno\\"
# glob 返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。
img_Lists = glob.glob(src_img_dir + '\*.jpg')  # 为图像路径列表
# print(img_Lists)

img_basenames = []  # 对应的是路径中的图像名字
for item in img_Lists:
    # 获取对应路径下文件的名字：os.path.basename
    img_basenames.append(os.path.basename(item))  # 图像名字
    # img_basenames输出为图像名字列表，包含后缀
    # print(img_basenames)
img_names = []  # e.g. 100
for item in img_basenames:
    # os.path.splitext()将文件名和扩展名分开：
    temp1, temp2 = os.path.splitext(item)  #
    img_names.append(temp1)  # img_names为图像名列表，不包含后缀
    # print(temp1)
for img in img_names:
    # 获取图像文件夹下中的每一幅图像（包含路径和后缀）
    im = Image.open((src_img_dir + '\\' + img + '.jpg'))
    width, height = im.size

    # open the crospronding txt file
    # splitlines()返回一个包含各行作为元素的列表。
    gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()  # 将txt中的每一行作为列表的元素，输出全部内容
    # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    # open()中的参数“w”打开一个文件只用于写入。
    # 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
    # 如果该文件不存在，创建新文件。
    xml_file = open((src_xml_dir + '\\' + img + '.xml'), 'w')  #
    # print(xml_file )输出为xml的路径+名字文件，处于可写入模式
    xml_file.write('<annotation>\n')  # 通过write()函数向文件中写入多行
    xml_file.write('    <folder>myPerson</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')
    xml_file.write('    <segmented>0</segmented>\n')
    # 批量读取xml中的内容
    # write the region of image on xml file
    i = 1
    for img_each_label in gt:  # gt 包含txt全部内容，以每行内容为一个元素的列表
        # 以空格为分割符的方式提取 gt=['ship1 539 355 563 391','ship2 397 25 416 48']
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        # print(spt) #spt 读取txt中的第一行内容，spt=['ship1','539','355','563','391']
        # spt打印['Images/s1.jpg', '391', '243', '428', '355', '426', '249', '468', '367', '']
        imax = len(spt)
        for i in range(0, imax - 1, 4):
            # print(str(spt[i + 1]))
            xml_file.write('<object>\n')
            xml_file.write('    <name>' + str(spt[i]) + '</name>\n')
            xml_file.write('    <pose>Unspecified</pose>\n')
            xml_file.write('    <truncated>0</truncated>\n')
            xml_file.write('    <difficult>0</difficult>\n')
            xml_file.write('    <bndbox>\n')
            xml_file.write('        <xmin>' + str(spt[i + 1]) + '</xmin>\n')
            # a=str(spt[i + 1]) #539
            # print(str(spt[i + 1]))
            xml_file.write('        <ymin>' + str(spt[i + 2]) + '</ymin>\n')
            xml_file.write('        <xmax>' + str(spt[i + 3]) + '</xmax>\n')
            xml_file.write('        <ymax>' + str(spt[i + 4]) + '</ymax>\n')
            xml_file.write('    </bndbox>\n')
            xml_file.write('</object>\n')
    xml_file.write('</annotation>')
