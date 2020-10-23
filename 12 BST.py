# _*_coding:utf-8_*_
# @Time    : 2020/9/8 22:45

'''二叉搜索树'''
from collections import deque
import random

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, li=None):            #初始化,传入列表li
        self.root = None                    #根本省置None
        if li :                             #若li传入
            for val in li:                  #遍历li中值，插入BST
                self.insert_no_rec(val)

    #递归方式插入/建树
    def insert_rec(self, node, val):
        if not node:                        #如果某方向节点为空
            node = BiTreeNode(val)          #建立节点
        elif val < node.data:               #插入的值小于根
            node.lchild = self.insert_rec(node.lchild, val)         #向左找节点
            node.lchild.parent = node       #更新node，把当前节点地址赋给当前节点的左孩子的父指针上
        elif val > node.data:               #同理
            node.lchild = self.insert_rec(node.rchild, val)
            node.rchild.parent = node
        return node

    #非递归方法插入/建树
    def insert_no_rec(self, val):
        p = self.root                   #获得根节点
        if not p:                       #如果没有根节点，就创建根节点
            self.root = BiTreeNode(val)
            return
        while True:                     #死循环
            if val < p.data:            #若输入值小于根
                if p.lchild:            #若存在左子树
                    p = p.lchild        #更新p，获得左孩子，再判断p和数据大小
                else:                   #如果没有左孩子
                    p.lchild = BiTreeNode(val)      #就新建一个左孩子节点
                    p.lchild.parent = p             #挂上双亲节点
                    return                          #节点插入完成返回
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:               #若插入值与根相同，直接返回
                return

    #查询递归版本
    def query_rec(self, node, val):
        if not node:            #如果找不到节点，返回None
            return None
        if node.data < val:
            return self.query_rec(node.lchild, val)
        elif node.data > val:
            return self.query_rec(node.rchild, val)
        else:
            return node

    #查询非递归方法
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.lchild
            elif p.data > val:
                p = p.rchild
            else:
                return p
        return None             #p找到空都找不到，就直接返回None

    '''删除操作'''
    #第1种情况，被删除节点是叶子节点,直接删除即可
    def __remove_node_1(self, node):
        if not node.parent:             #如果node的双亲节点不存在
            self.root = None            #则根节点为空
        if node == node.parent.lchild:  #如果node是其双亲节点的左孩子
            node.parent.lchild = None   #则将其双亲节点的左孩子指针置空即可完成删除node节点操作
        else:
            node.parent.rchild = None

    #第2种情况的之一，被删除节点只有一个左孩子
    def __remove_node_2_1(self, node):
        if not node.parent:                     #若删除的节点没有双亲节点
            self.root = node.lchild             #根节点移步到其左孩子
            node.lchild.parent = None           #断开节点左孩子的双亲
        elif node == node.parent.lchild:        #如果要删除的节点是其双亲的左孩子
            node.parent.lchild = node.lchild    #节点的左孩子地址挂给节点双亲的左孩子指针上
            node.lchild.parent = node.parent    #节点的双亲地址挂给节点左孩子的双亲节点上
        else:                                   #要删除的节点是其双亲的节点的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    #第2种情况之二，本删除的节点只有一个右孩子
    def __remove_node_2_2(self, node):
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:        #要删除的节点是其双亲的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:                                   #要删除的节点是其双亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    #节点删除算法，涵盖了情况1和情况2
    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:         #情况1
                self.__remove_node_1(node)
            elif not node.rchild:                           #情况2之一
                self.__remove_node_2_1(node)
            elif not node.lchild:                           #情况2之二
                self.__remove_node_2_2(node)
            else:                                           #情况3，被删除的节点有两个叶子节点
                min_node = node.rchild                      #需要把删除节点的右子树的最下方的左孩子作为新根节点
                while min_node.lchild:                      #只要右子树的左孩子存在，就执行下去
                    min_node = min_node.lchild
                node.data = min_node.data                   #把右子树最下层左孩子的值取出，放入node数据域中
                #删除min_code
                if min_node.rchild:
                    self.__remove_node_2_2(min_node)
                else:
                    self.__remove_node_1(min_node)



    '''前序遍历'''
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    '''中序遍历'''
    def in_order(self, root):
        if root:
            self.pre_order(root.lchild)
            print(root.data, end=',')
            self.pre_order(root.rchild)

    '''后序遍历'''
    def post_order(self, root):
        if root:
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
            print(root.data, end=',')

    '''层次遍历'''
    def level_order(self, root):
        self.queue = deque()
        self.queue.append(root)
        while len(self.queue) > 0:
            node = self.queue.popleft()
            print(node.data, end=',')
            if node.lchild:
                self.queue.append(node.lchild)
            if node.rchild:
                self.queue.append(node.rchild)

# tree = BST([2,5,3,7,8,3,2,1,7,5,6,9,4,1])
tree = BST([4, 6, 7, 9, 2, 1, 3, 6, 5, 8])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)
print('')
tree.post_order(tree.root)
print('\n')

li = list(range(0, 500, 2))
random.shuffle(li)

tree = BST(li)
print(tree.query_rec(tree.root, 3))