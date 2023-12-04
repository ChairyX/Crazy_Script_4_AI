import os

def delete_empty_txt(out_txt_floder, out_img_floder):
    txt_list = os.listdir(out_txt_floder)
    for txt_name in txt_list:
        #  去除.txt后缀
        name = txt_name[:-4]
        #  txt完整路径
        txt_path = out_txt_floder + "\\" + txt_name
        #  对应图像完整路径
        img_path = out_img_floder + "\\" + name + ".png"
        with open(txt_path, "r") as f:
            #  读取txt全部内容,然后关闭
            data = f.read()
            f.close()
            #  若该txt为空,删除txt及其对应图像
            if data == "":
                os.remove(txt_path)
                os.remove(img_path)
                print('{}为空，已被删除.'.format(name))


#  切割后数据集的标签文件存放文件夹
out_txt_floder = r'-----'
#  切割得到的图像数据集存放文件夹
out_img_floder = r'-----'

delete_empty_txt(out_txt_floder, out_img_floder)