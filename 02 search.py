# _*_coding:utf-8_*_
# @Time    : 2020/9/2 0:32

'''查找算法'''
from cal_time import *

'''顺序查找，时间复杂度O(n)'''
@cal_time
def linear_search(li, var):
    for ind, v in enumerate(li):
        if v == var:
            return ind
        else:
            return None

'''二分查找，折半查找，要求输入的列表是顺序表O(logn) '''
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:    # 候选区存在
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: # val待查找的值在mid左侧
            right = mid - 1
        else:               # val待查找的值在mid右侧
            left = mid + 1
    else:
        return None

li = list(range(10000000))
linear_search(li, 389000)
binary_search(li, 389000)
