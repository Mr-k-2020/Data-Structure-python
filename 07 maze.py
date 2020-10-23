# _*_coding:utf-8_*_
# @Time    : 2020/9/4 22:39

#迷宫本体
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#方向
dirs = [lambda x,y : (x+1, y),
        lambda x,y : (x-1, y),
        lambda x,y : (x, y+1),
        lambda x,y : (x, y-1)]
'''栈实现'''
def maze_deep_first(x1, y1, x2, y2):        #(x1,y1)和(x2,y2)分别是迷宫起点终点
    stack = []                  #建立路径存入栈中
    stack.append((x1, y1))
    while(len(stack)>0):        #判断栈是否为空
        curNode = stack[-1]     #栈顶元素即curNode表示当前节点
        if curNode[0] == x2 and curNode[1] == y2:       #判断是否已经到达终点
            for p in stack:
                print(p)
            return True
        #(x,y)的四个方向(x-1,y);(x-1,y);(x,y+1);(x,y-1)
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:         #如果下一个节点能走
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2          #已走过的点置一个标记
                break       #如果能走，就继续走下去，跳出方向选择
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False

'''队列实现'''
from collections import deque

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])
    realpath.reverse()          #逆序反转
    for node in realpath:
        print(node)

def maza_bread_path(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y2, -1))      #queue中每个元素有三个值，横纵坐标和引导它输入队列的节点索引，起点输入队列，将引导起点入队的索引置-1
    path = []
    while len(queue) > 0:           #当队不空时
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[0] == y2:       #到达终点
            print_r(path)           #输出路径
            return True
        for dir in dirs:        #所有方向都找一遍，能走的统统入队
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path)-1))       #后续节点入队，记录引它入队的节点索引，即path中最后一个节点位置
                maze[nextNode[0]][nextNode[1]] = 2      #标记已走过的路径
    else:       #队空时直接判定没有路
        print("没有路")
        return False

# maze_deep_first(2, 2, 8, 8)
maza_bread_path(2, 2, 8, 8)