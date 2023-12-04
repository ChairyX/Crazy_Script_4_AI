import cv2
import os


#  图像宽不足裁剪宽度,填充至裁剪宽度
def fill_right(img, size_w):
    size = img.shape
    #  填充值为数据集均值
    img_fill_right = cv2.copyMakeBorder(img, 0, 0, 0, size_w - size[1],
                                        cv2.BORDER_CONSTANT, value=(107, 113, 115))
    return img_fill_right


#  图像高不足裁剪高度,填充至裁剪高度
def fill_bottom(img, size_h):
    size = img.shape
    img_fill_bottom = cv2.copyMakeBorder(img, 0, size_h - size[0], 0, 0,
                                         cv2.BORDER_CONSTANT, value=(107, 113, 115))
    return img_fill_bottom


#  图像宽高不足裁剪宽高度,填充至裁剪宽高度
def fill_right_bottom(img, size_w, size_h):
    size = img.shape
    img_fill_right_bottom = cv2.copyMakeBorder(img, 0, size_h - size[0], 0, size_w - size[1],
                                               cv2.BORDER_CONSTANT, value=(107, 113, 115))
    return img_fill_right_bottom


#  图像切割
#  img_floder 图像文件夹
#  out_img_floder 图像切割输出文件夹
#  size_w 切割图像宽
#  size_h 切割图像高
#  step 切割步长
# def image_split(img_floder, out_img_floder, size_w=1000, size_h=1000, step=800):
#     img_list = os.listdir(img_floder)
#     count = 0
#     for img_name in img_list:
#         number = 0
#         #  去除.png后缀
#         name = img_name[:-4]
#         img = cv2.imread(img_floder + "\\" + img_name)
#         size = img.shape
#         #  若图像宽高大于切割宽高
#         if size[0] >= size_h and size[1] >= size_w:
#             count = count + 1
#             for h in range(0, size[0] - 1, step):
#                 start_h = h
#                 for w in range(0, size[1] - 1, step):
#                     start_w = w
#                     end_h = start_h + size_h
#                     if end_h > size[0]:
#                         start_h = size[0] - size_h
#                         end_h = start_h + size_h
#                     end_w = start_w + size_w
#                     if end_w > size[1]:
#                         start_w = size[1] - size_w
#                     end_w = start_w + size_w
#                     cropped = img[start_h: end_h, start_w: end_w]
#                     #  用起始坐标来命名切割得到的图像，为的是方便后续标签数据抓取
#                     name_img = name + '_' + str(start_h) + '_' + str(start_w)
#                     cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
#                     number = number + 1
#         #  若图像高大于切割高,但宽小于切割宽
#         elif size[0] >= size_h and size[1] < size_w:
#             print('图片{}需要在右面补齐'.format(name))
#             count = count + 1
#             img0 = fill_right(img, size_w)
#             for h in range(0, size[0] - 1, step):
#                 start_h = h
#                 start_w = 0
#                 end_h = start_h + size_h
#                 if end_h > size[0]:
#                     start_h = size[0] - size_h
#                     end_h = start_h + size_h
#                 end_w = start_w + size_w
#                 cropped = img0[start_h: end_h, start_w: end_w]
#                 name_img = name + '_' + str(start_h) + '_' + str(start_w)
#                 cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
#                 number = number + 1
#         #  若图像宽大于切割宽,但高小于切割高
#         elif size[0] < size_h and size[1] >= size_w:
#             count = count + 1
#             print('图片{}需要在下面补齐'.format(name))
#             img0 = fill_bottom(img, size_h)
#             for w in range(0, size[1] - 1, step):
#                 start_h = 0
#                 start_w = w
#                 end_w = start_w + size_w
#                 if end_w > size[1]:
#                     start_w = size[1] - size_w
#                     end_w = start_w + size_w
#                 end_h = start_h + size_h
#                 cropped = img0[start_h: end_h, start_w: end_w]
#                 name_img = name + '_' + str(start_h) + '_' + str(start_w)
#                 cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
#                 number = number + 1
#         #  若图像宽高小于切割宽高
#         elif size[0] < size_h and size[1] < size_w:
#             count = count + 1
#             print('图片{}需要在下面和右面补齐'.format(name))
#             img0 = fill_right_bottom(img, size_w, size_h)
#             cropped = img0[0: size_h, 0: size_w]
#             name_img = name + '_' + '0' + '_' + '0'
#             cv2.imwrite('{}/{}.png'.format(out_img_floder, name_img), cropped)
#             number = number + 1
#         print('{}.png切割成{}张.'.format(name, number))
#     print('共完成{}张图片'.format(count))


#  txt切割
#  out_img_floder 图像切割输出文件夹
#  txt_floder txt文件夹
#  out_txt_floder txt切割输出文件夹
#  size_w 切割图像宽
#  size_h 切割图像高
def txt_split(out_img_floder, txt_floder, out_txt_floder, size_h=1000, size_w=1000):
    img_list = os.listdir(out_img_floder)
    for img_name in img_list:
        #  去除.png后缀
        name = img_name[:-4]
        #  得到原图像(也即txt)索引 + 切割高 + 切割宽
        name_list = name.split('_')
        txt_name = name_list[0]
        h = int(name_list[1])
        w = int(name_list[2])
        txtpath = txt_floder + "\\" + txt_name + '.txt'
        out_txt_path = out_txt_floder + "\\" + name + '.txt'
        f = open(out_txt_path, 'a')
        #  打开txt文件
        with open(txtpath, 'r') as f_in:
            lines = f_in.readlines()
            #  逐行读取
            for line in lines:
                splitline = line.split(' ')
                if len(splitline) < 3: continue
                else:
                    label = splitline[8]
                    difficult = splitline[9]
                    x1 = int(float(splitline[0]))
                    y1 = int(float(splitline[1]))
                    x2 = int(float(splitline[2]))
                    y2 = int(float(splitline[3]))
                    x3 = int(float(splitline[4]))
                    y3 = int(float(splitline[5]))
                    x4 = int(float(splitline[6]))
                    y4 = int(float(splitline[7]))
                    if w <= x1 <= w + size_w and w <= x2 <= w + size_w and \
                            w <= x3 <= w + size_w and w <= x4 <= w + size_w and \
                            h <= y1 <= h + size_h and h <= y2 <= h + size_h and \
                            h <= y3 <= h + size_h and h <= y4 <= h + size_h:
                        f.write('{} {} {} {} {} {} {} {} {} {}'.format(int(x1 - w),
                                                                       int(y1 - h), int(x2 - w), int(y2 - h), int(x3 - w),
                                                                       int(y3 - h), int(x4 - w), int(y4 - h),
                                                                       label, difficult))
        f.close()
        print('{}.txt切割完成.'.format(name))


#  图像数据集文件夹
img_floder = r'F:\DataSets_OBB\DOTA\images'
#  切割得到的图像数据集存放文件夹
out_img_floder = r'F:\DataSets_OBB\DOTA_D\images'
#  txt数据集文件夹
txt_floder = r'F:DataSets_OBB\DOTA\labels'
#  切割后数据集的标签文件存放文件夹
out_txt_floder = r'F:\DataSets_OBB\DOTA_D\labels'
#  切割图像宽
size_w = 1000
#  切割图像高
size_h = 1000
#  切割步长,重叠度为size_w - step
step = 800

# image_split(img_floder, out_img_floder, size_w, size_h, step)
txt_split(out_img_floder, txt_floder, out_txt_floder, size_h, size_w)
