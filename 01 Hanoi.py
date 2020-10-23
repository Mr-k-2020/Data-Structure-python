# _*_coding:utf-8_*_
# @Time    : 2020/9/2 0:31

'''汉诺塔，简单递归算法'''
def hanoi(n, a, b, c):
    '''把n个盘子从a经过b移动到c'''
    if n>0:
        hanoi(n-1, a, c, b)
        print("Moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)

hanoi(3, 'A', "B", "C")