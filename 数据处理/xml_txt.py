# *_* coding : UTF-8 *_*
# 文件名称   ：xml_txt.py.py
# 功能描述   ：xml文件转换成dota能识别的txt文件
#             就是把x1,y1,x2,y2,x3,y3,x4,y4的xml转换成x1 y1 x2 y2 x3 y3 x4 y4 className difficult

import os
import xml.etree.ElementTree as ET
import cv2
import numpy as np


def edit_xml(xml_file):
    if ".xml" not in xml_file:
        return
    tree = ET.parse(xml_file)
    root = tree.getroot()

    txt = xml_file.replace(".xml", ".txt")
    bmp = xml_file.replace(".xml", ".bmp")  # 图片格式
    src = cv2.imread(bmp, 1)

    with open(txt, 'w') as wf:
        for i in root.iter('object'):
            x0text = ""
            y0text = ""
            x1text = ""
            y1text = ""
            x2text = ""
            y2text = ""
            x3text = ""
            y3text = ""
            difficult_text = ""
            className = ""

            className = i.find('name').text
            if i.find('difficult').text in [0, 1, 2]:
                difficult_text = i.find('difficult').text  # 赋值difficult
            else:
                difficult_text = 0

            x0text = i.find('polygon').find('x1').text
            y0text = i.find('polygon').find('y1').text

            x1text = i.find('polygon').find('x2').text
            y1text = i.find('polygon').find('y2').text

            x2text = i.find('polygon').find('x3').text
            y2text = i.find('polygon').find('y3').text

            x3text = i.find('polygon').find('x4').text
            y3text = i.find('polygon').find('y4').text

            points = np.array([[int(float(x0text)), int(float(y0text))],
                               [int(float(x1text)), int(float(y1text))],
                               [int(float(x2text)), int(float(y2text))],
                               [int(float(x3text)), int(float(y3text))]], np.int32)
            cv2.polylines(src, [points], True, (255, 0, 0))  # 画任意多边

            wf.write(
                "{} {} {} {} {} {} {} {} {} {}\n".format(float(x0text), float(y0text), float(x1text),
                                                         float(y1text), float(x2text), float(y2text),
                                                         float(x3text), float(y3text),
                                                         className, difficult_text))


if __name__ == '__main__':
    dirs = r"----------"  # 此文件夹中必须既要放jpg图片集又要放图片对应的xml文件不然会报打不开文件的错误！！
    filelist = os.listdir(dirs)
    for file in filelist:
        edit_xml(os.path.join(dirs, file))
