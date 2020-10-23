# _*_coding:utf-8_*_
# @Time    : 2020/9/2 0:27
#装饰器，用于计算程序运行时间

import time

def cal_time(func):     #传入函数
    def wrapper(*args, **kwargs):       #声明wrapper的参数
        t1 = time.time()
        result = func(*args, **kwargs)  #传入func原本参数
        t2 = time.time()
        print("%s runing time: %s secs." % (func.__name__, t2-t1))      #函数名和计算时间
        return result
    return wrapper

# def cal_time(func):
#     def wrapper(*args):
#         t1 = time.time()
#         result = func(*args)
#         t2 = time.time()
#         print("Totle time: {:.15f} s".format(t2 - t1))
#         return result
#     return wrapper