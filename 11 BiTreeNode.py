# _*_coding:utf-8_*_
# @Time    : 2020/9/8 21:44

'''定义二叉树节点'''
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

#建立二叉树
root = e
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

# print(root.lchild.rchild.data)            #找某个节点

'''二叉树遍历'''
'''前序遍历'''
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

'''中序遍历'''
def in_order(root):
    if root:
        pre_order(root.lchild)
        print(root.data, end=',')
        pre_order(root.rchild)

'''后序遍历'''
def post_order(root):
    if root:
        pre_order(root.lchild)
        pre_order(root.rchild)
        print(root.data, end=',')

'''层次遍历'''
from collections import deque

def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

print("前序遍历")
pre_order(root)
print('')
print("中序遍历")
in_order(root)
print('')
print("后序遍历")
post_order(root)
print('')
print('层次遍历')
level_order(root)