# _*_coding:utf-8_*_
# @Time    : 2020/9/9 9:36

from BST import BiTreeNode, BST

class AVLNode(BiTreeNode):                  #AVL树节点由二叉搜索树节点继承构成
    def __init__(self, data):
        BiTreeNode.__init__(self, data)     #继承BiTreeNode的全部属性
        self.bf = 0                         #新增属性bf

class AVLTree(BST):
    def __init__(self, li):
        BST.__init__(self, li)              #继承全部属性

    #左旋操作
    def rotate_left(self, p, c):            #p为需要调整的子树根，c为需要调整的子树节点
        s = c.lchild            #临时存储c的左孩子
        p.rchild = s            #把s赋给p的右孩子，即把c的左孩子赋给p的右孩子
        if s:                   #s可以为None，如果s不为空
            s.parent = p        #需要把s的双亲指针挂在p上
        c.lchild = p            #把p作为c的左孩子
        p.parent = c            #把p的双亲作为c
        p.bf = 0                #p和c的平衡因子置0
        c.bf = 0
        return c                #返回调整后的根节点

    # 右旋操作
    def rotate_right(self, p, c):  # p为需要调整的子树根，c为需要调整的子树节点
        s = c.rchild        # 临时存储c的右孩子
        p.lchild = s        # 把s赋给p的左孩子，即把c的右孩子赋给p的左孩子
        if s:               # s可以为None，如果s不为空
            s.parent = p    # 需要把s的双亲指针挂在p上
        c.rchild = p    # 把p作为c的右孩子
        p.parent = c    # 把p的双亲作为c
        p.bf = 0        # p和c的平衡因子置0
        c.bf = 0
        return c

    #先右旋再左旋操作
    '''
    在G子树中插入节点
    调整前
                                   p
                s1(len=h)                             c
                                            G                   s4(len=h)
                                s2(len=h or h-1)   s3(len=h or h-1)
                                    ||
                                  \ || /
                                    \/
    调整后
                                       G
                      P                                   C
           s1(len=h)       s2(len=h or h-1)   s3(len=h or h-1)       s4(len=h)                            
    '''
    def rotate_right_left(self, p, c):
        #先右旋
        g = c.lchild
        s3 = g.rchild     #为什么移动s3，因为右旋操作需要移动s3
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g
        #再左旋
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g
        #更新平衡因子
        if g.bf > 0:        #如果新根的bf>0,则左重右轻
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:      #如果新根的bf<0,则左轻右重
            p.bf = 0
            c.bf = 1
        g.bf = 0            #如果新根的bf=0，左右平衡
        return g            #返回调整后的根节点

    def rotate_left_right(self, p, c):
        #先z左旋
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g
        #再右旋
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        #更新平衡因子
        if g.bf > 0:        #如果新根的bf>0,则左重右轻
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:      #如果新根的bf<0,则左轻右重
            p.bf = 1
            c.bf = 0
        g.bf = 0            #如果新根的bf=0，左右平衡
        return g            #返回调整后的根节点

    #先把数据插入树中，在调整，复用BST中的插入代码
    def insert_no_rec(self, val):
        p = self.root  # 获得根节点
        if not p:  # 如果没有根节点，就创建根节点
            self.root = BiTreeNode(val)
            return
        while True:  # 死循环，来一个值就执行
            if val < p.data:  # 若输入值小于根
                if p.lchild:  # 若存在左子树
                    p = p.lchild  # 更新p，获得左孩子，再判断p和数据大小
                else:  # 如果没有左孩子
                    p.lchild = BiTreeNode(val)  # 就新建一个左孩子节点
                    p.lchild.parent = p  # 挂上双亲节点
                    node = p.lchild # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val == p.data
                return
        #更新每个节点的BF平衡因子
        while node.parent:      #当插入的节点存在双亲节点的时候
            if node.parent.lchild == node:      #如果插入节点在左子树，那么传递是从左子树来的，那么左子树就更沉了
                #更新node.parent 的bf -= 1
                if node.parent.bf < 0:          #原来node.parent.bf == -1,节点插入并更新后变成-2
                    #做旋转，看node哪边沉
                    g = node.parent.parent      #为了链接旋转后的子树，先存需要挂载的地址
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    #记得把n和g连起来
                elif node.parent.bf > 0:    #原来node.parent.bf = 1,更新之后变成0
                    node.parent.bf = 0
                    break
                else:   #原来node.parent.bf = 0，更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent      #往上找，进一步做调整
                    continue
            else:   #传递从右子树来，那么右子树就更沉了
                #更新node，parent，bf += 1
                if node.parent.bf > 0:  #原来node.parent.bf == 1, 更新后变成2
                    #做旋转，看node哪边沉
                    g = node.parent.parent  #为了旋转之后的子树
                    if node.bf < 0: #node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:           #node.bf = -1
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:    # 原来的node.parent.bf = -1， 更新后变成0
                    node.parent.bf = 0
                    break
                else:                       #原来node.parent.bf = 0, 更新后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue
            #链接旋转后的子树
            n.parent = g
            if g:   #g不空
                if node.parent == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break

tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)