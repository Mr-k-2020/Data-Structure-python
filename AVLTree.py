# _*_coding:utf-8_*_
# @Time    : 2020/9/10 10:33

class Node(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=0
class AVLTree(object):
    def __init__(self):
        self.root=None
    def find(self,key):
        if self.root is None:
            return None
        else:
            return self._find(key,self.root)
    def _find(self,key,node):
        if node is None:
            return None
        elif key<node.key:
            return self._find(key,self.left)
        elif key>node.key:
            return self._find(key,self.right)
        else:
            return node
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)
    def _findMin(self,node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)
    def _findMax(self,node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node
    def height(self,node):
        if node is None:
            return -1
        else:
            return node.height

    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    def put(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._put(key, self.root)

    def _put(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self._put(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
        elif key > node.key:
            node.right = self._put(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.doubleRightRotate(node)
                else:
                    node = self.singleRightRotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def delete(self, key):
        self.root = self.remove(key, self.root)

    def remove(self, key, node):
        if node is None:
            raise KeyError('Error,key not in tree')
        elif key < node.key:
            node.left = self.remove(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif key > node.key:
            node.right = self.remove(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self.remove(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self.remove(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node


# class TreeNode(object):
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#         self.height = 0
# class AVLTree(object):
#     def __init__(self):
#         self.root = None
#     def find(self, key):
#         if not self.root:
#             return None
#         else:
#             return self._find(key, self.root)
#     def _find(self, key, node):
#         if not node:
#             return None
#         elif key < node.data:
#             return self._find(key, node.left)
#         elif key > node.data:
#             return self._find(key, node.right)
#         else:
#             return node
#     def findMin(self):
#         if self.root is None:
#             return None
#         else:
#             return self._findMin(self.root)
#     def _findMin(self, node):
#         if node.left:
#             return self._findMin(node.left)
#         else:
#             return node
#     def findMax(self):
#         if self.root is None:
#             return None
#         else:
#             return self._findMax(self.root)
#     def _findMax(self, node):
#         if node.right:
#             return self._findMax(node.right)
#         else:
#             return node
#     def height(self, node):
#         if node is None:
#             return -1
#         else:
#             return node.height
#     #在node节点的左孩子k1的左子树添加了新节点，左旋转
#     def singleLeftRotate(self, node):
#         k1 = node.left
#         node.left = k1.right
#         k1.right = node
#         node.height = max(self.height(node.right), self.height(node.left)) + 1
#         k1.height = max(self.height(k1.left), node.height) + 1
#         return k1
#     #在node节点的右孩子k1的右子树添加了新节点，右旋转
#     def singleRightRotate(self, node):
#         k1 = node.right
#         node.right = k1.left
#         k1.left = node
#         node.height = max(self.height(node.right), self.height(node.left)) + 1
#         k1.height = max(self.height(k1.right), node.height) + 1
#         return k1
#     #在node节点的左孩子的右子树添加了新节点，先左后右
#     def doubleRightRotate(self, node):
#         node.right = self.singleLeftRotate(node.right)
#         return self.singleRightRotate(node)
#     #在node节点的右孩子的左子树添加了新节点,先右后左
#     def doubleLeftRotate(self, node):
#         node.left = self.singleRightRotate(node.left)
#         return self.singleLeftRotate(node)
#     def insert(self, key):
#         if not self.root:
#             self.root = TreeNode(key)
#         else:
#             self.root = self._insert(key, self.root)
#     def _insert(self, key, node):
#         if node is None:
#             node = TreeNode(key)
#         elif key < node.data:
#             node.left = self._insert(key, node.left)
#             if (self.height(node.left) - self.height(node.right)) == 2:
#                 if key < node.left.data:
#                     node = self.singleLeftRotate(node)
#                 else:
#                     node = self.doubleLeftRotate(node)
#         elif key > node.data:
#             node.right = self._insert(key, node.right)
#             if (self.height(node.right) - self.height(node.left)) == 2:
#                 if key > node.right.data:
#                     node = self.singleRightRotate(node)
#                 else:
#                     node = self.doubleRightRotate(node)
#         node.height = max(self.height(node.right), self.height(node.left)) + 1
#         return node
#     def delete(self, key):
#         if self.root is None:
#             raise KeyError('Error,empty tree')
#         else:
#             self.root = self._delete(key, self.root)
#     def _delete(self, key, node):
#         if node is None:
#             raise KeyError('Error,key not in tree')
#         elif key < node.data:
#             node.left = self._delete(key, node.left)
#             if (self.height(node.right) - self.height(node.left)) == 2:
#                 if self.height(node.right.right) >= self.height(node.right.left):
#                     node = self.singleRightRotate(node)
#                 else:
#                     node = self.doubleRightRotate(node)
#             node.height = max(self.height(node.left), self.height(node.right)) + 1
#         elif key > node.data:
#             node.right = self._delete(key, node.right)
#             if (self.height(node.left) - self.height(node.right)) == 2:
#                 if self.height(node.left.left) >= self.height(node.left.right):
#                     node = self.singleLeftRotate(node)
#                 else:
#                     node = self.doubleLeftRotate(node)
#             node.height = max(self.height(node.left), self.height(node.right)) + 1
#         elif node.left and node.right:
#             if node.left.height <= node.right.height:
#                 minNode = self._findMin(node.right)
#                 node.key = minNode.key
#                 node.right = self._delete(node.key, node.right)
#             else:
#                 maxNode = self._findMax(node.left)
#                 node.key = maxNode.key
#                 node.left = self._delete(node.key, node.left)
#             node.height = max(self.height(node.left), self.height(node.right)) + 1
#         else:
#             if node.right:
#                 node = node.right
#             else:
#                 node = node.left
#         return node