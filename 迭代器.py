# _*_coding:utf-8_*_
# @Time    : 2020/9/7 18:15

'''用迭代器模拟for循环'''
lst = ['张三', "李四", "王五"]
#for 循环内部大致工作机制
it = lst.__iter__()     #拿到对象迭代器
while True:             #死循环
    try:                #尝试执行
        obj = it.__next__()     #拿到数据
        print(obj)
    except StopIteration:       #如果出现StopIteration
        break                   #执行操作

