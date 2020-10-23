# _*_coding:utf-8_*_
# @Time    : 2020/9/10 15:17

''''''
'''问题1 现金100，50，20，5，1，给一个金额，组合数字'''
t = [100, 50, 20, 5, 1]
def change_money(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

print('----------问题1----------')
print(change_money(t, 378))

'''问题2 如何取商品使获益最大
   在有限的质量下尽可能多装贵的东西，允许只拿部分商品的一部分'''
print('----------问题2----------')
#分数背包
def fractional_backpack(goods, w):
    goods_index = []
    for i, (prince, weight) in enumerate(goods):
        goods_index.append((i, (prince, weight)))
    goods_index.sort(key=lambda x: x[1][0] / x[1][1], reverse=True)  # 根据商品单位价值排序
    m = [0 for _ in range(len(goods_index))]
    total_v = 0
    for i in range(len(goods_index)):
        if w >= goods_index[i][1][1]:
            m[i] = 1
            total_v += goods_index[i][1][0]
            w -= goods_index[i][1][1]
        else:
            m[i] = w / goods_index[i][1][1]
            total_v += m[i] * goods_index[i][1][0]
            w = 0
            break
    mm = []
    for i in range(len(m)):
        mm.append((m[i], goods_index[i]))
    mm.sort(key=lambda x : x[1])
    return total_v, mm

goods = [(60, 10), (120, 30), (100, 20)]        #商品元组，第一个是总价值，第二个是总重量
total_v, m = fractional_backpack(goods, 50)
print(total_v, m)

'''n个非负整数，按字符串拼接方式拼接成一个整数，使整数最大'''
print('----------问题3----------')
li = [32, 94, 128, 1286, 6, 71]
lst = list(map(str, li))
def bubble(lst):
    change = True
    while change:
        for j in range(len(lst)):
            for i in range(1, len(lst)):
                if lst[i-1] + lst[i] < lst[i] + lst[i-1]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                else:
                    change = False
    return "".join(lst)
print(bubble(lst))

'''活动选择问题
   多个活动占用同一片场地，每个活动有开始和结束时间，如何分配顺序使活动最多
   思路，每次选择结束时间最早的活动'''
print('----------问题4----------')
activaties = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]    #前者开始时间，后者结束时间
#保证活动按照结束时间排序的
activaties.sort(key=lambda x:x[1])

def activity_selesction(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:       #当前活动开始时间大于前一活动结束的时刻
            res.append(a[i])
    return res

print(activity_selesction(activaties))