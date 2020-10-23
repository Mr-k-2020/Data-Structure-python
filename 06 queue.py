# _*_coding:utf-8_*_
# @Time    : 2020/9/4 20:32

class Queue:
    def __init__(self, size=100):
        self.queue = [0 for i in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    #判断队空
    def is_empty(self):
        return self.rear == self.front

    #判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# q = Queue(5)
# for i in range(4):
#     q.push(i)
# print(q.is_filled())

'''内置模块实现队列'''
from collections import deque       #deque科创建双向队列

#.append(),popleft()进行单向队列操作
q = deque([1,2,3,4,5], 5)
q.append(6)         #队尾入队
print(q.popleft())  #队首出队

#appendleft(),pop()进行双向队列操作
q.appendleft(1)     #队首入队
print(q.pop())      #队尾出队

'''双向队列可用于输出文件后若干行'''
def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q
for line in tail(5):
    print(line, end='')