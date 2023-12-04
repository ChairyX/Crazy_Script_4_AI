
# 功能描述： DOTA格式，选出需要的类别

import os
import cv2
import shutil

catogary = ['small-vehicle',
            'large-vehicle',
            'helicopter',
            'container-crane',
            'plane'
            'ship'
            ]  # 列表


def customname(fullname):
    """返回不带后缀的文件名"""
    return os.path.basename(os.path.splitext(fullname)[0])

def getFileFromRoot(dir):
    """获得每个文件的完整路径，包括后缀"""
    allfiles = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            allfiles.append(file_path)
    return allfiles


if __name__ == '__main__':
    root = r'F:\DataSets_OBB\DOTA_original'
    raw_pic_path = os.path.join(root, 'images')
    raw_lab_path = os.path.join(root, 'labels')
    bridge_pic = os.path.join(root, 'DOTA/images')
    bridge_lab = os.path.join(root, 'DOTA/labels')

    label_list = getFileFromRoot(raw_lab_path)
    for label_path in label_list:
        n = 0
        f = open(label_path, 'r')
        lines = f.readlines()
        split_lines = (line.strip().split(' ') for line in lines)
        for i, split_line in enumerate(split_lines):
            if i in [0, 1]:  # 标签文本前两行为格式及高度，无用
                continue
            catogary_name = split_line[8]  # 类别
            if catogary_name in catogary:
                n = n + 1
                if n >= 1:  # 所要求类别目标数量达到两个就可以将该图像挑选出来
                    name = customname(label_path)  # 不带后缀的标签文件名
                    old_label_path = label_path
                    old_img_path = os.path.join(raw_pic_path, name + '.jpg')

                    img = cv2.imread(old_img_path)
                    new_lab_path = os.path.join(bridge_lab, name + '.txt')
                    new_pic_path = os.path.join(bridge_pic, name + '.jpg')

                    cv2.imwrite(new_pic_path, img)
                    shutil.copyfile(old_label_path, new_lab_path)
