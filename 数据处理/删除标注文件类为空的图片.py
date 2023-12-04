# 移动标签为空的xml，并同步移动相应图片
import os
import xml.etree.ElementTree as ET
import shutil


# 设置原始标签路径
origin_ann_dir = r'F:\shujuji\DOTA_split\0Annotations\\'
# 设置新标签路径
new_ann_dir = r'F:\shujuji\DOTA_split\Annotations\\'

origin_pic_dir = r'F:\shujuji\DOTA_split\0JPEGImages\\'
new_pic_dir = r'F:\shujuji\DOTA_split\JPEGImages\\'

if not os.path.exists(new_ann_dir):
    os.makedirs(new_ann_dir)
if not os.path.exists(new_pic_dir):
    os.makedirs(new_pic_dir)

k = 0
p = 0
q = 0
# os.walk游走遍历目录名
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):  
    for filename in filenames:
        print("process...")
        k = k + 1
        print(k)
        # 获取原始xml文件绝对路径，isfile()检测是否为文件 isdir检测是否为目录
        if os.path.isfile(r'%s%s' % (origin_ann_dir, filename)):
            # 如果是，获取绝对路径（重复代码）
            origin_ann_path = os.path.join(r'%s%s' % (origin_ann_dir, filename))  
            new_ann_path = os.path.join(r'%s%s' % (new_ann_dir, filename))
            # ET是一个xml文件解析库，ET.parse（）打开xml文件。parse--"解析"
            tree = ET.parse(origin_ann_path)
            # 获取根节点
            root = tree.getroot() 
            if (root.findall('object')):
                p = p + 1
            else:
                print(filename)
                old_xml = origin_ann_dir + filename
                new_xml = new_ann_dir + filename
                old_pic = origin_pic_dir + filename.replace("xml", "jpg")
                new_pic = new_pic_dir + filename.replace("xml", "jpg")
                q = q + 1
                shutil.move(old_pic, new_pic)
                shutil.move(old_xml, new_xml)
print("ok, ", p)
print("empty, ", q)