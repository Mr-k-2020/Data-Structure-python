# _*_coding:utf-8_*_
# @Time    : 2020/9/11 16:34

''''''
'''最大公约数'''
def gcb(a, b):      #递归方法
    if b == 0:
        return a
    else:
        return gcb(b, a % b)

def gcb2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
print(gcb2(12, 16))

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcb(a, b)
        self.a /= x
        self.b /= x

    def gcb(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgc(self, a, b):
        x = self.gcb(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgc(b, a)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)