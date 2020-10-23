# _*_coding:utf-8_*_
# @Time    : 2020/9/2 22:03

import  os

def read(path, ceng):
    lst = os.listdir(path)
    for name in lst:
        real_path = os.path.join(path, name)
        if os.path.isdir(real_path):
            print("\t"*ceng, name)
            read(real_path, ceng+1)
        else:
            print('\t'*ceng, name)

read("../", 0)