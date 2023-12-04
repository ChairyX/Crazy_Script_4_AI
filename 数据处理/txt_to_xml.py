import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

# 图片文件夹，后面的/不能省
img_path = r"C:\Users\14437\Desktop\VOC2007\VOC2007\JPEGImages\\"

# txt文件夹，后面的/不能省
labels_path = r"C:\Users\14437\Desktop\VOC2007\VOC2007\Annotations\\"

# xml存放的文件夹，后面的/不能省
annotations_path = r"C:\Users\14437\Desktop\VOC2007\VOC2007\xml\\"

labels = os.listdir(labels_path)

# 类别
classes = ['nishui','yisi','safe']

# 图片的高度、宽度、深度
sh = sw = sd = 0

def write_xml(imgname, sw, sh, sd, filepath, labeldicts):
    '''
    imgname: 没有扩展名的图片名称
    '''

    # 创建Annotation根节点
    root = ET.Element('Annotation')

    # 创建filename子节点，无扩展名
    ET.SubElement(root, 'filename').text = str(imgname)

    # 创建size子节点
    sizes = ET.SubElement(root,'size')
    ET.SubElement(sizes, 'width').text = str(sw)
    ET.SubElement(sizes, 'height').text = str(sh)
    ET.SubElement(sizes, 'depth').text = str(sd)

    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')
        ET.SubElement(objects, 'name').text = labeldict['name']
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
        ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
        ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
        ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')


for label in labels:
    with open(labels_path + label, 'r') as f:
        img_id = os.path.splitext(label)[0]
        contents = f.readlines()
        labeldicts = []
        for content in contents:
            # 这里要看你的图片格式了，我这里是jpg，注意修改
            img = np.array(Image.open(img_path + label.strip('.txt') + '.jpg'))

            # 图片的高度和宽度
            sh, sw, sd = img.shape[0], img.shape[1], img.shape[2]
            content = content.strip('\n').split()
            x = float(content[1])*sw
            y = float(content[2])*sh
            w = float(content[3])*sw
            h = float(content[4])*sh

            # 坐标的转换，x_center y_center width height -> xmin ymin xmax ymax
            new_dict = {'name': classes[int(content[0]) - 1],
                        'difficult': '0',
                        'xmin': x+1-w/2,
                        'ymin': y+1-h/2,
                        'xmax': x+1+w/2,
                        'ymax': y+1+h/2
                        }
            labeldicts.append(new_dict)
        write_xml(img_id, sw, sh, sd, annotations_path + label.strip('.txt') + '.xml', labeldicts)



