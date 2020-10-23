# _*_coding:utf-8_*_
# @Time    : 2020/9/4 18:57

'''建立栈，作为一个类'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty.")

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise IndexError("Top of stack have no element.")

    def is_empty(self):
        return len(self.stack) == 0


'''括号匹配算法'''
def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}     #建立字典，根据右括号指定左括号
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:           #遇到左括号统一入栈
            stack.push(ch)
        else:                               #遇到的不是左括号，则遇到的全是右括号
            if stack.is_empty():            #检查栈是否已空，若空，False
                return False
            elif stack.get_top() == match[ch]:  #若栈顶与读到的匹配，栈顶出栈
                stack.pop()
            else:                           #若栈顶与读到的不匹配，False
                return False
    if stack.is_empty():                    #字符串读完，若栈已空，则括号都匹配
        return True
    else:                                   #否则不匹配
        return False

stack = Stack()
stack.get_top()