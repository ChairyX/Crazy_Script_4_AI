import numpy as np
import glob
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom

'''
第一步，将xml文件和图片重新命名
'''


# 获取文件夹中bmp图片的数量
def getDirImageNum(path):
    bmpDirImagesNum = 0
    for bmpfile in os.listdir(path):
        if os.path.splitext(bmpfile)[1] == '.png':
            bmpDirImagesNum += 1
    return bmpDirImagesNum


# 获取文件夹中xml文件的数量
def getDirXmlNum(path):
    xmlDirXmlNum = 0
    for xmlfile in os.listdir(path):
        if os.path.splitext(xmlfile)[1] == '.xml':
            xmlDirXmlNum += 1
    return xmlDirXmlNum


inputpath1 = r"F:\shujuji\data\10\JPEGImages0\\"
inputpath2 = r'F:\shujuji\data\10\Annotations0\\'

outpath1 = r"F:\shujuji\data\10\JPEGImages\\"
outpath2 = r'F:\shujuji\data\10\Annotations\\'

file_name = os.listdir(inputpath2)

error = []
for item in file_name:
    print(item)
    o_imap = inputpath1 + item.split('.')[0] + ".png"
    o_xmlp = inputpath2 + item.split('.')[0] + ".xml"
    i = getDirImageNum(outpath1)  # 表示bmp文件的命名是从当前输出文件夹中的bmp文件数目开始的
    if os.path.exists(o_imap) and os.path.exists(o_xmlp):
        i = i + 1
        new_name = '10x' + format(str(i), '0>5s') + '.png'
        dst1 = os.path.join(os.path.abspath(outpath1), new_name)  # 为000001.jpg
        os.rename(o_imap, dst1)
        dst2 = os.path.join(os.path.abspath(outpath2), '10x' + format(str(i), '0>5s') + '.xml')  # 为000000.xml形式，想要的格式
        try:
            dom = xml.dom.minidom.parse(o_xmlp)
            root = dom.documentElement
            # 获取标签对path之间的值并赋予新值j
            # 文件夹赋值
            # root.getElementsByTagName('folder')[0].firstChild.data = "VOC2007"

            # 获取标签对filename之间的值并赋予新值j
            root.getElementsByTagName('filename')[0].firstChild.data = new_name

            # 将修改后的xml文件保存,xml文件修改前后的路径
            # 打开并写入
            with open(o_xmlp, 'w') as fh:
                dom.writexml(fh)
            os.rename(o_xmlp, dst2)
            print('converting %s to %s ...' % (o_xmlp, dst2))
        except:
            error.append(new_name)
            continue
# 如果有出错的文件，error++
print(len(error))
