# _*_coding:utf-8_*_
# @Time    : 2020/9/8 0:31

g = (i for i in range(5))
print(g)

#生成器 -> 迭代器 -> 可迭代对象 -> for循环
#遍历生成器 for循环法
for item in g:
    print(item)
#list tuple set 可直接把生成器拿空
print(list(g))

print("----------------以上归于认识生成器-----------------")

def func():     #类比为卖票窗口
    print(111)
    yield 222

g = func()              #黄牛1
g1 = (i for i in g)     #黄牛2
g2 = (i for i in g1)    #黄牛3

'''func是窗口，黄牛1从窗口买票，黄牛2从黄牛1买票，黄牛3从黄牛2买票'''
print(list(g))          #若黄牛1买了票，黄牛2、3都是空
print(list(g1))
print(list(g2))

print(list(g2))          #若黄牛3买了票，黄牛1、2都是空
print(list(g))
print(list(g1))