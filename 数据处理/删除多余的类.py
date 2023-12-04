import os
import xml.etree.ElementTree as ET
import tqdm


def del_delete_eq_1(xml_path):
    # 从xml文件中读取，使用getroot()获取根节点，得到的是一个Element对象
    tree = ET.parse(xml_path)
    root = tree.getroot()

    objects = root.find('objects')

    for object1 in objects.findall('object'):
        deleted = str(object1.find("possibleresult").find('name').text)

        if deleted in ['Roundabout', 'Baseball Field', 'Basketball Court',
                       'Football Field', 'Tennis Court', 'Intersection', 'Bridge']:
            objects.remove(object1)

    tree.write(xml_path)


def main():
    root_dir = r"F:\shujuji\FAIR1M\labelXml"
    xml_path_list = [os.path.join(root_dir, x) for x in os.listdir(root_dir)]

    # 使用tqdm显示进程
    for xml in tqdm.tqdm(xml_path_list):
        del_delete_eq_1(xml)


if __name__ == '__main__':
    main()
