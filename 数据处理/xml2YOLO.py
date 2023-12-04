import os
import xml.etree.ElementTree as ET

# 设置数据集路径和YOLOv5格式的标注文件保存路径
data_dir = r'F:\data\10\Annotations\\'
output_dir = r'F:\data\10\txt\\'

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历数据集文件夹
for xml_file in os.listdir(data_dir):
    if xml_file.endswith('.xml'):
        # 解析XML文件
        tree = ET.parse(os.path.join(data_dir, xml_file))
        root = tree.getroot()

        # 提取图像宽度和高度
        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)

        # 创建YOLOv5格式的TXT文件
        txt_file = os.path.splitext(xml_file)[0] + '.txt'
        with open(os.path.join(output_dir, txt_file), 'w') as txt:
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                if class_name == 'airplane' or class_name == 'plane':
                    cname = '0'
                else:
                    cname = '1'
                x_min = int(obj.find('bndbox/xmin').text)
                y_min = int(obj.find('bndbox/ymin').text)
                x_max = int(obj.find('bndbox/xmax').text)
                y_max = int(obj.find('bndbox/ymax').text)

                # 计算中心点和归一化坐标
                x_center = (x_min + x_max) / (2 * width)
                y_center = (y_min + y_max) / (2 * height)
                width_norm = (x_max - x_min) / width
                height_norm = (y_max - y_min) / height

                # 将信息写入TXT文件
                txt.write(f'{cname} {x_center} {y_center} {width_norm} {height_norm}\n')

print("已将XML数据集转换为YOLOv5格式的TXT文件。")