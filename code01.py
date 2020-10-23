# _*_coding:utf-8_*_
# @Time    : 2020/9/1 23:31

'''汉诺塔，简单递归算法'''
def hanoi(n, a, b, c):
    '''把n个盘子从a经过b移动到c'''
    if n>0:
        hanoi(n-1, a, c, b)
        print("Moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)

# hanoi(3, 'A', "B", "C")
'''查找算法'''



'''顺序查找，时间复杂度O(n)'''
def linear_search(li, var):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None

'''二分查找，折半查找，要求输入的列表是顺序表O(logn) '''
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

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 3))