# _*_coding:utf-8_*_
# @Time    : 2020/9/6 16:52

class Node:         #将链表封装到类，传入一个参数，指针默认为空
    def __init__(self, item):
        self.item = item
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a)            #打印a地址
print(a.next)       #a之后节点地址
print(b)            #b节点地址
print(a.item)       #打印a节点值
print(a.next.item)  #打印a下一节点值

'''创建链表'''
#头插法创建链表
def create_linklist_head(li):
    head = Node(li[0])          #列表首元素作为头
    for element in li[1:]:      #循环列表值
        node = Node(element)    #列表值建立节点
        node.next = head        #头指针地址赋给传入链表的节点地址
        head = node             #重新对头节点赋值
    return head

#尾插法创建链表
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)    #列表值建立节点
        tail.next = node        #新节点地址存入尾指针所指向节点的指针中
        tail = node             #更新尾指针
    return head

'''双向链表'''
#定义节点类
class TwoWayNode:
    #初始化节点属性
    def __init__(self, data):
        self.data = data        #数据域
        self.prev = None        #前驱指针
        self.next = None        #后继指针

    def getData(self):          #获得节点数据域
        return self.data

    def setData(self, data):    #设置节点值
        self.data = data

    def getNext(self):          #获得后继指针指向的地址
        return self.next

    def getPrev(self):          #获得前驱指针指向的地址
        return self.prev

#定义双向链表类
class TwoWayLinklist:
    #初始化双向链表的3个属性
    def __init__(self):
        self.head = None        #双向链表头指针
        self.tail = None        #尾指针
        self.length = 0         #链表长度

    # 判断链表是否为空
    def isEmpty(self):
        return self.head == None    #头指针为0则链表为空

    #从后端插入节点
    def append(self, item):
        if self.length == 0:    #如果链表为空
            node = TwoWayNode(item)     #实例一个节点，称为node
            self.head = node    #链表头指针指向节点
            self.tail = node    #链表尾指针也指向节点
            self.length = 1     #链表长度置为1
            return
        node = TwoWayNode(item) #实例一个节点，称为node
        tail = self.tail        #根据链表原来的尾指针获得链表尾节点，链表尾节点称为tail
        tail.next = node        #把新节点的地址赋给原链表尾节点的后继指针
        node.prev = tail        #原链表尾节点的地址赋给新节点的前驱指针
        self.tail = node        #更新链表的尾指针
        self.length += 1        #链表长度加1

    #链表中间插入节点
    def insert(self, index, item):      #参数：插入位置和元素
        length = self.length            #获取链表长度
        #判断插入位置是否合法，若不合法则插入失败
        if (index<0 and abs(index)>length) or (index>0 and index >= length):
            return False                #插入失败
        # 通过负数索引找找正数索引
        if index < 0:
            index = index + length
        # 若index=0，则再链表首插入节点
        if index == 0:
            node = TwoWayNode(item)     #实例一个节点，称为node
            if self.head != None:       #如果链表头不空
                self.head.prev = node   #把新节点的地址赋给原链表头节点的前驱指针上
            else:                       #如果链表头空
                self.tail = Node        #链表尾指向新节点
            node.next = self.head       #把原链表头指针指向的节点地址赋给新指针的后继节点上
            self.head = node            #新节点地址给链表头指针
            self.length += 1
            return True                 #返回
        #若在链表尾插入节点
        if index == length - 1:
            return self.append(item)    #返回 用append方法
        #若插入位置合法、不在表首不在表尾则执行以下步骤
        node1 = self.head               #获得原链表的头指针指向的节点，记为node1
        for i in range(0, index):       #根据index挨个找节点
            node1 = node1.next          #循环结束，找到插入位置前一个节点node1
        node2 = node1.next              #插入位置后一个节点node2

        node = TwoWayNode(item)         #创建插入节点为node
        node.prev = node1               #把node1地址赋值给node前驱指针
        node.next = node2               #把node2地址赋值给node后继指针
        node1.next = node               #把node的地址赋值给node1的后继指针
        node2.prev = node               #把node的地址赋值给node2的前驱指针

        self.length += 1                #链表长度加1
        return True

    #根据节点数据获取链表节点
    def get(self, data):
        node = self.head                #拿到链表头节点
        for i in range(self.length):    #循环链表长度
            if node.data == data:       #如果输入的数据与节点数据域数据匹配
                return node             #返回节点
            else:                       #否则找下一个节点
                node = node.next
        else:
            return False

    #根据下标获取链表节点
    def getByIndex(self, index):
        if index >= self.length:        #如果索引超出范围，返回False
            return False
        if index == 0:                  #如果索引=0，返回头节点
            return self.head
        now = self.head                 #不满足以上条件，把头节点给now
        for i in range(self.length):    #根据链表长度，循环遍历整个链表
            if i == index:
                return now
            now = now.next

    #根据下标更新节点数据
    def setData(self, index, data):
        if index >= self.length:
            return False
        if index == 0:
            self.head.data = data
        now = self.head
        for i in range(self.length):
            if i == index:
                now.data = data
                return True
            now = now.next

    #根据下标删除节点
    def remove(self, index):
        if index >= self.length:                #索引超出链表长度
            return False
        if index == 0:                          #索引为0，指向链表头节点
            self.head = self.head.next          #头节点的后继指针赋给链表头指针
            if self.length != 1:                #当链表长度不为1时，新的头节点的前驱指针置None
                self.head.prev = None
            self.length -= 1                    #链表长度减1
            return True
        if index == self.length - 1:            #索引指向尾节点
            self.tail = self.tail.prev          #链表尾节点的前驱指针中地址赋给链表尾指针
            self.tail.next = None               #新的尾节点的后继指针置None
            self.length -= 1                    #链表长度减1
            return True
        now = self.head                         #索引最一般的情况，不满足以上所有条件
        for i in range(self.length):            #根据链表长度循环
            if i == index:                      #根据链挨个找节点
                now.next.prev = now.prev        #当前节点的前驱指针赋给当前节点下一个节点的前驱
                now.prev.next = now.next        #当前节点的后继指针赋给当前节点上一个节点的后继
                self.length -= 1                #链表长度减1
                return True
            now = now.next

    #清空链表，链表头尾指针置空，长度置0
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    #打印链表中的数据，遍历
    def __str__(self):          #重写__str__方法
        string = ''
        node = self.head
        for i in range(self.length):
            string += str(node.data) + '/'
            node = node.next
        return string


#遍历打印链表
def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next

