# _*_coding:utf-8_*_
# @Time    : 2020/9/5 14:05
import random

# def bubble_topk(li, k):
#     for i in range(k):
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j+1], li[j] = li[j], li[j+1]
#     return li[-5:]
#
# li = list(range(1000))
# random.shuffle(li)
# print(bubble_topk(li, 10))

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:       #j>=防止指针越界
            li[j + gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d = d // 2

# import random
# li = list(range(10))
# random.shuffle(li)
# print(li)
# shell_sort(li)
# print(li)

class Fib:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        print('__iter__ called')
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        print('__next__ called')
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

# for i in Fib(3):
#     print(i)
# 输出
# __iter__ called
# __next__ called
# 0
# __next__ called
# 1
# __next__ called
# 1
# __next__ called
# 2
# __next__ called

# import time
#
# list1 = [ i for i in range(1,100000)]
# set1 = set(list1)
#
# start = time.time()
# for i in (range(10000)):
#     -1 in list1
#     #  -1 in set1
# end = time.time()
# print(end-start)

