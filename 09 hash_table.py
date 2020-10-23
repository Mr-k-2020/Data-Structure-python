# _*_coding:utf-8_*_
# @Time    : 2020/9/6 22:37

'''用拉链法创建哈希表'''
class LinkList:             #创建哈希函数后面的链表类
    class Node:             #节点函数，嵌套入链表类中
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:             #创建链表迭代器类
        def __init__(self, node):       #初始化一个节点
            self.node = node

        def __next__(self):             #执行下一步操作
            if self.node:               #如果链表中有节点
                cur_node = self.node    #获得当前节点
                self.node = cur_node.next   #把node给安排了，把cur_node的下一个元素地址给node
                return cur_node.item    #返回cur_node的元素值域
            else:                       #如果下一个节点找不到了，node=False
                raise StopIteration     #返回一个错误代码

        def __iter__(self):             #迭代自身
            return self

    def __init__(self, iterable=None):  #链表迭代器初始化方法
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:               #如果头节点不存在，创建头尾指针
            self.head = s
            self.tail = s
        else:                           #如果头节点存在
            self.tail.next = s          #把新节点接到尾指针后
            self.tail = s               #更新尾指针

    def extend(self, iterable):         #链表追加方法
        for obj in iterable:
            self.append(obj)

    def find(self, obj):                #找节点
        for n in self:                  #建的链表迭代器类中有__iter__和__next__方法，所以链表本身可以迭代，每次返回一个节点
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):                 #链表迭代
        return self.LinkListIterator(self.head)

    def __repr__(self):             #重写__repr___方法，输出字符串
        #这里self是而可迭代对象，通过map函数转化元素为字符串
        return "<<" + ", ".join(map(str, self)) + '>>'


class HashTabel:                        #建哈希表
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]         #新建的哈希表本身就是调用链表类建的

    def h(self, k):                     #建哈希函数 方法
        return k % self.size

    def insert(self, k):                #插入哈希表前先找表中是否有重复
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert")
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


lk = LinkList([1, 2, 3, 4, 5])
for element in lk:
    print(element)
print(lk)

ht = HashTabel()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)

print(",".join(map(str, ht.T)))