# _*_coding:utf-8_*_
# @Time    : 2020/9/7 18:15

'''生成器示例'''
#每次生成一件衣服
def order():
    for i in range(10000):
        yield f"衣服{i}"

g = order()             # g作为一个生成器
print(g.__next__())     # 每次__next__(),执行到一次yield
print(g.__next__())     # 每次__next__(),执行到一次yield
print(next(g))

'''生成器改进，每次生成50件衣服'''
def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst
            lst = []

g = order()
lst1 = g.__next__()
print(lst1)

lst2 = g.__next__()
print(lst2)


def func():
    print("111")
    a = yield "酥饼"
    print("222", a)
    b = yield "韭菜盒子"
    print("333", b)
    yield "红酒"

g = func()
r1 = g.__next__()
print(r1)
r2 = g.send("哈哈")
print(r2)
r3 = g.send("呵呵")
print("r3=", r3)

'''函数返回如下
111         33行
酥饼        34行 yield 返回 酥饼
222 哈哈      35行 打印222，并且43行的时候用send给34行的a传入“哈哈”
韭菜盒子        36行 yield返回 韭菜盒子
333 呵呵        37行 打印333，并且45行用send给36行的b传入“呵呵”
r3= 红酒        46行打印r3=，38行返回“红酒”
'''