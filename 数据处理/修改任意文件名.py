
#  修改任意文件名字
import os

fold_dir = r'------'  # 需要修改的文件所在的文件夹
filename = os.listdir(fold_dir)  # 该文件夹中文件的名称
print(filename)  # 在控制台输出原文件名称

for number, temp in enumerate(filename):  # 编号，和得到各文件名
    new_filename = 'c' + format(str(number + 1), '0>4s') + '.txt'  # 新文件名（注意跟上文件后缀名）
    os.rename(fold_dir + '/' + temp, fold_dir + new_filename)  # 文件重命名后替换原文件名
    print(new_filename)  # 在控制台输出替换后的文件名称
