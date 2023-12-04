
# 功能描述： 将FAIR1M格式的xml转换为DOTA的格式


import os
import xml.etree.ElementTree as ET
import cv2
import numpy as np


def edit_xml(xml_file):
    if ".xml" not in xml_file:
        return
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objs = root.find('objects').findall('object')

    txt = xml_file.replace(".xml", ".txt")
    tif = xml_file.replace(".xml", ".tif")  # 图片格式
    src = cv2.imread(tif, 1)

    with open(txt, 'w') as wf:

        for i in range(len(objs)):

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

            className = objs[i][3][0].text
            difficult_text = 0

            if len(objs) != 0:
                a, b = objs[i][4][0].text.split(',')
                # print(int(float(a)), int(float(b)))

                x0text, y0text = objs[i][4][0].text.split(',')

                x1text, y1text = objs[i][4][1].text.split(',')

                x2text, y2text = objs[i][4][2].text.split(',') 

                x3text, y3text = objs[i][4][3].text.split(',')

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
    dirs = r"------"  # 此处的xml1130文件夹中必须既要放jpg图片集又要放图片对应的xml文件不然会报打不开文件的错误！！
    filelist = os.listdir(dirs)
    for file in filelist:
        edit_xml(os.path.join(dirs, file))

