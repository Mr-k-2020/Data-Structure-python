# _*_coding:utf-8_*_
# @Time    : 2020/9/8 20:19

'''树结构模拟文件管理'''
class Node:         #创建每一层文件夹
    def __init__(self, name, type='dir'):           #文件类型默认文件夹
        self.name = name            #文件名
        self.type = type            #文件类型
        self.children = []          #文件夹下的文件，可能是文件也可能是文件夹，用列表存储
        self.parent = None          #文件夹上一层文件，父节点

    def __repr__(self):             #文件夹名输出
        return self.name

# n = Node("Hello")           #第1个文件名
# n2 = Node("World")          #第2个文件名
# n.children.append(n2)       #第1个文件下放第2个文件
# n2.parent = n               #第2个文件的上一层链接到第1个文件

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")               #初始化根目录，根目录在 /
        self.now = self.root                #把根目录赋给当前位置

    #建文件夹
    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    #展示当前文件下的文件名
    def ls(self):
        return self.now.children            #Node类中已添加__repr__方法，返回即可输出文件夹名

    #进入文件夹
    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":                   #如果输入 ../ 返回上一层
            self.now = self.now.parent      #返回上层目录
            return
        for child in self.now.children:     #遍历当前层的所有文件
            if child.name == name:          #找到要访问的文件夹
                self.now = child            #进入下一层作为当前层
                return
        raise ValueError("Invalid dir")     #如果找不到就返回错误

tree = FileSystemTree()         #建文件结构
tree.mkdir("var/")              #建var文件夹
tree.mkdir("bin/")              #建bin文件夹
tree.mkdir("usr/")              #建usr文件夹

tree.cd("bin/")                 #进入到bin文件夹下
tree.mkdir("python/")           #创建python文件夹

tree.cd("../")                  #返回上一层

print(tree.ls())                #展示当前层所有文件