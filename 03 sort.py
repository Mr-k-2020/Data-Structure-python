# _*_coding:utf-8_*_
# @Time    : 2020/9/2 11:47

import random

'''冒泡排序，每趟根据相邻数字大小交换位置，O(n2)'''
def bubule_sort(li):
    for i in range(len(li)-1):      #i 代表需要排序趟数，即尾端有序区长度，0~n-1，当有序区为n-1，排序完毕
        exchange = False            #标志位，用于判断每一趟是否需要排序
        for j in range(len(li)-i-1):    #泡泡的指针，作用在无序区，指针范围0~n-i-1
            if li[j] > li[j+1]:         #根据大小交换相邻位置
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True     #如果有排序操作，则标志位置True
        print(li)
        if not exchange:            #如果没有进行排序，则直接输出
            return

# li = [random.randint(0, 10000) for i in range(10)]
# print(li)
# bubule_sort(li)

'''选择排序'''
def select_sort_sample(li):     #调用了内置函数，时间复杂度不可控，而且还需要一片新存储空间 O(n2)
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li):            #改进的选择排序，不需要新空间，时间复杂度O(n2)
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i, len(li)):
            if li[j+1] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)

# print(select_sort_sample(li))
# select_sort(li)

'''插入排序'''           #时间复杂度O(n2)
def insert_sort(li):    #原理就是以第一个元素为有序区，第二个元素开始往左依次插入有序区的位置
    for i in range(1, len(li)):         #i为无序区第一个元素
        tmp = li[i]
        j = i - 1                       #j为有序区最后一个元素
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = tmp
        print(li)

# import random
# li = [i for i in range(10)]
# random.shuffle(li)
# insert_sort(li)
# print(li)

# insert_sort(li)


'''快速排序'''          #先取一个数，放在左边都比它小，右边都比他大的位置上，然后左右递归,时间复杂度O(nlogn)
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:        #从右端找比tmp小的数
            right -= 1          #right往左走一步
        li[left] = li[right]    #把右端值写在左空位
        while left < right and li[left] <= tmp:         #从右端找比tmp大的数
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li, left, right):           #找到第一个元素该去的位置：元素比左侧所有数大，比右侧所有数小
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)        #递归，对中点左侧所有数进行快排
        _quick_sort(li, mid+1, right)       #递归，对中点右侧所有数进行快排

def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

# import random
# li = [i for i in range(100)]
# random.shuffle(li)
# print(li)
# quick_sort(li)
# print(li)


'''堆排序，基于二叉树，时间复杂度O(nlogn)'''
def sift(li, low, high):
    '''
    用于构建大根堆
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆最后元素位置
    '''
    i = low             #最开始指向根节点
    j = 2 * i + 1       #j开始时左孩子
    tmp = li[low]       #把堆顶存起来
    while j <= high:    #若j没过最后一个节点，i指向的是父节点
        if j + 1 <= high and li[j+1] > li[j]:   #如果有右孩子，而且右孩子比左孩子大
            j = j + 1       #j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j           #往下看一层
            j = 2 * i + 1
        else:               #tmp更大，把tmp放到i的位置上
            li[i] = tmp     #把tmp放到某一父节点上
            break
    else:                   #若j过了最后的节点，则i指向的是叶子节点
        li[i] = tmp         #把tmp放到叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):       # i表示所有父节点的下标
        #倒序遍历所有子树，每个子树均调整成堆
        sift(li, i, n-1)    #第二个参数为low指根，第二个参数为high指整棵树最后的叶子节点
                            # sift函数中high参数的目的即为用于判断j是否越界，即j是否指向列表之外
                            # 因此，最后叶子节点（列表最后元素）代替当前节点子树的最后叶子，不会产生问题
    # 初步构建大根堆，然后依次从根出数，调用sift向下继续调整成堆
    for i in range(n-1, -1, -1):            #i 指向当前堆最后一个元素，每次循环i向前指一个位置
        #倒序遍历根
        li[0], li[i] = li[i], li[0]         #交换根与最后节点的位置
        sift(li, 0, i-1)    #i-1是新的high

# li = [i for i in range(100)]
# import random
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)

'''内置模块实现堆排序'''
import heapq
import random

li = list(range(100))
random.shuffle(li)
print(li)
heapq.heapify(li)       #建立小根堆
n = len(li)
for i in range(n):      #小根堆挨个出数
    print(heapq.heappop(li), end = ',')
print(end='\n')
print("以上是python内部的堆排序")

'''TopK问题，用堆排序解决，时间复杂度O(nlogk)
   TopK问题的关键在于整体数据n和K的大小
   若n>>k,用堆排序O(nlogk)
   若n>k,用冒泡排序O(nk)'''
def sift_min(li, low, high):        #建立小根堆，与大根堆只改了两个符号
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li [j]
            i = j
            j = 2 * i +1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def sift_topk(li, k):
    heap = li[0:k]
    n = len(heap)
    # 针对列表前k个数建小根堆
    for i in range((n-2)//2-1, -1, -1):
        sift_min(heap, i, k-1)
    # 依次遍历k之后的数，与堆顶元素比较，选大的数作为堆顶，再调整
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift_min(heap, 0, k-1)
    # 小根堆出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_min(heap, 0, i-1)
    return heap

def bubble_topk(li, k):
    for i in range(k):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
    return li[-5:]

# li = list(range(1000))
# random.shuffle(li)
# print(sift_topk(li, 10))
# print(bubble_topk(li, 10))

'''归并排序，时间复杂度O(nlogn)，空间复杂度O(n)'''
def merge(li, low, mid, high):
    '''
    假设列表分左右两段，左右两段段内有序，使用归并排序，分别比较左右两段大小，存入临时ltmp
    :param li: 列表
    :param low: 列表左端起始索引
    :param mid: 左段串最后一个元素索引，+1即为右段串起始索引
    :param high: 列表终止索引
    '''
    i = low         #左段串开始指针
    j = mid + 1     #右段串开始指针
    ltmp = []
    while i <= mid and j <= high:
        #依次比较左右串大小，把小的放到ltmp
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    #当左段或右段串其中一个输出完了，另一个串则全部按顺序放到ltmp中即可
    while i <= mid:     #当左段串还有剩余
        ltmp.append(li[i])
        i += 1
    while j <= high:    #当右段串还有剩余
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp  #把临时列表用切片方法放回列表中，用于递归

def merge_sort(li, low, high):
    #先拆列表，递归（拆到每块只剩一个元素，单个元素本身有序，归并）
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

# li = list(range(10))
# random.shuffle(li)
# print(li)
# merge_sort(li, 0, len(li)-1)
# print(li)

'''希尔排序：基于插入排序的改进'''
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
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

'''计数排序，前提数据重复较多，而且已知数据分布范围，O(n)'''
def count_sort(li, max_count=100):      #知道数字分布在0~100之间
    #创建列表，包含全部数据，索引为列表元素值名称，对应值为出现次数
    count = [0 for _ in range(max_count+1)]       #初始化，每个元素出现个数都是0
    for val in li:
        count[val] += 1
    li.clear()          #清空原列表
    for ind, val in enumerate(count):           #同时取出别表索引和值
        #每个值出现几次，就在原列表中添加几次
        for i in range(val):
            li.append(ind)

# import random
# li = [random.randint(0, 100) for _ in range(1000)]
# print(li)
# count_sort(li)
# print(li)

'''桶排序，生成若干个桶，每个桶所存数据有范围，桶挨个存放，桶内数据有序，统一输出'''
def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]        #创建很多桶，每个桶对所存数据有限制，桶索引范围0~99
    for var in li:
        # 用于确定每个数据需要放置的桶的编号
        i = min(var // (max_num // n), n-1)
        #根据数值确定进入第几个桶，有个问题是，串中最大的数10000，经过计算需要进第100个桶
        #但是创建的很多桶没有没有索引第100的桶，因此，10000需要放到第99个桶中
        #因此根据数值选桶序号，遇到最大值取(100,99)中最小的数作为索引
        #min的作用仅针对10000，不针对其他值
        buckets[i].append(var)      #把值放到对应地桶中
        #保持桶内有序，使用的方法基于冒泡排序，从桶后端依次放入一个数，每次放入，都使用冒泡排序调整顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []                #创建新空间，用于输出排序结果
    for buc in buckets:
        sorted_li.extend(buc)     #每个桶中数据有序，依次连接每个桶的数据，即可获得有序数据
    return sorted_li

import random
li = [random.randint(0, 10) for _ in range(20)]
print(li)
print(bucket_sort(li))

'''基数排序'''
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:      #从个位开始入桶进行排序，循环直至到最大位
        buckets = [[] for _ in range(10)]
        for var in li:
            # 取相应位上的数值，方法，先整除再取余
            digit = (var // 10 ** it) % 10      # 9872 ,当it=2时,digit=8，方法9872//10^2=98 98%10=8
            buckets[digit].append(var)          #挨个入桶
        li.clear()
        for buc in buckets:
            li.extend(buc)                      #取数
        it += 1