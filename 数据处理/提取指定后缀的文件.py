
 
import os
import sys
import os.path
from shutil import copy
 
for dirpath,dirnames,filenames in os.walk(r"F:\shujuji\DataSets_pro\UCAS_AOD\PLANE\\"):
    for filename in filenames:
        if os.path.splitext(filename)[1] == ".png": # 指定后缀
            filepath = os.path.join(dirpath, filename)
            print(filepath)
            copy(filepath, r"F:\shujuji\DataSets_pro\UCAS_AOD\images\\"+filename)