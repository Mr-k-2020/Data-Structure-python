# _*_coding:utf-8_*_
# @Time    : 2020/9/11 8:59

'''动态规划'''
'''斐波那契数列'''
print('----------问题1-------------')
def fibnacci_no_rec(n):
    lst = [1, 1]
    if n <= 2:
        return 1
    else:
        for i in range(n-2):
            lst.append(lst[-1] + lst[-2])
        return lst[-1]

def fibnacci_rec(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibnacci_rec(n-1) + fibnacci_rec(n-2)

print(fibnacci_no_rec(10))
print(fibnacci_rec(10))

'''从钢条切割问题看动态规划'''
print('----------问题2-------------')
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

#递推式1 res = max(pn, r1+rn-1, r2+rn-2+...+rn-1+r1)
def cut_rod_rec_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_rec_1(p, i) + cut_rod_rec_1(p, n-i))
        return res

#递推式2 res = max(pi+rn-i)
def cut_rod_res_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_rod_res_2(p, n-i))
        return res

#动态规划算法解决钢条问题
def cut_rod_dp(p, n):
    r = [0]         #从小到大把每个长度的最有情况记录下来
    for i in range(1, n+1):
        res = 0
        #递推式 res = max(pi+rn-i) 与递推式2相同
        for j in range(1, i+1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]

#输出最优切割方案
print('----------问题4-------------')
def cut_rod_extend(p, n):
    r = [0]     #从小到大把每个长度的最好的情况记录下来
    s = [0]     #切下一刀后左边的剩余长度
    for i in range(1, n+1):
        res_r = 0       #价格最大值
        res_s = 0       #价格最大值对应方案的左边不再继续切割部分的长度
        for j in range(1, i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans

r, s = cut_rod_extend(p, 9)
print(s)
print(cut_rod_dp(p, 9))
print(cut_rod_solution(p, 9))

# print(cut_rod_rec_1(p, 9))
# print(cut_rod_res_2(p, 9))
# print(cut_rod_dp(p, 9))

print('----------问题4-------------')
'''最大子序列'''
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            if x[i-1] != y[j-1]:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    for _ in c:
        print(_)
    return c[m][n]

def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]       #最大子序列匹配长度
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]       #每个匹配位置方向来源,左上方来为1，上方2，左方3
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    return c[m][n], b

def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


x = "ABCBDAB"
y= "BDCABA"
# lcs_num = lcs_length(x, y)
# print(lcs_num)

print(lcs_trackback(x, y))