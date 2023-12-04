import os
import cv2
import math


def convert(size, box):
    x_center = box[1] + box[3] / 2.0
    y_center = box[2] + box[4] / 2.0
    # 归一化
    x = x_center / int(size[0])
    y = y_center / int(size[1])
    # 求宽高并归一化
    w = box[3] / size[0]
    h = box[4] / size[1]
    return (int(box[0]), x, y, w, h)


def fun(str_num):
    before_e = float(str_num.split('e')[0])
    sign = str_num.split('e')[1][:1]
    after_e = int(str_num.split('e')[1][1:])

    if sign == '+':
        float_num = before_e * math.pow(10, after_e)
    elif sign == '-':
        float_num = before_e * math.pow(10, -after_e)
    else:
        float_num = None
        print('error: unknown sign')
    return float_num


def makexml(picPath, txtPath, yolo_paths):  # txt所在文件夹路径，yolo文件保存路径，图片所在文件夹路径
    """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
    """

    files = os.listdir(txtPath)
    for i, name in enumerate(files):
        print(name)

        yolo_txt_path = os.path.join(yolo_paths, name.split(".")[0]
                                     + ".txt")
        txtFile = open(txtPath + name)
        with open(yolo_txt_path, 'w') as f:
            txtList = txtFile.readlines()
            img = cv2.imread(picPath + name[0:-4] + ".png")
            Pheight, Pwidth, _ = img.shape

            for j in txtList:

                oneline = j.strip().split("\t")
                try:
                    int(oneline[9])
                except ValueError:
                    a = fun(oneline[9])
                else:
                    a = int(oneline[9])

                try:
                    int(oneline[10])
                except ValueError:
                    b = fun(oneline[10])
                else:
                    b = int(oneline[10])

                try:
                    int(oneline[11])
                except ValueError:
                    c = fun(oneline[11])
                else:
                    c = int(oneline[11])

                try:
                    int(oneline[12])
                except ValueError:
                    d = fun(oneline[12])
                else:
                    d = int(oneline[12])

                oneline = (1, a, b, c, d)
                box = convert((Pwidth, Pheight), oneline)
                f.write(
                    str(box[0]) + " " + str(box[1]) + " " + str(box[2]) + " " + str(box[3]) + " " + str(box[4]) + '\n')


if __name__ == "__main__":
    picPath = r"F:\shujuji\UCAS_AOD\JPEGImages\\"  # 图片所在文件夹路径，后面的/一定要带上
    txtPath = r"F:\shujuji\UCAS_AOD\txt\\"  # txt所在文件夹路径，后面的/一定要带上
    yolo = r"F:\shujuji\UCAS_AOD\Annotations\\"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, txtPath, yolo)
