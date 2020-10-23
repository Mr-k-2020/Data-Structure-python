# _*_coding:utf-8_*_
# @Time    : 2020/9/7 18:14

'''装饰器雏形'''
def wrapper(fn):
    def inner():
        print("这里是执行前")
        fn()
        print("这里是执行后")
    return inner            #这里加括号和不加括号是两个意思
                            #return inner() 返回inner函数执行结果
                            #return inner   返回inner函数，并不执行
#装饰器雏形，但一般不这么用
# def add():
#     print("新增函数")
# add = wrapper(add)      #wrapper内传入不加括号，加了括号就成执行函数了，装饰器赋给add
# add()

'''语法糖,用wrapper给下层函数装饰'''
@wrapper
def add():
    print("新增函数")

add()

print("-------------以上为装饰器雏形------------")

'''通用装饰器，记下背住'''
def wrapper(fn):
    def inner(*args, **kwargs):
        '''在执行目标函数之前'''
        ret = fn(*args, **kwargs)
        '''在执行目标函数之后'''
        return ret
    return inner

@wrapper
def target():       #定义目标函数
    pass


''' 
装饰器应用
用户操作前验证是否登录，没登录请登录，确保登录后执行操作
'''
flag = False        #默认用户没登录

def login_verify(fn):       #装饰器
    def inner(*args, **kwargs):
        while 1:    #死循环，反复验证用户是否登录成功
            if flag:
                ret = fn(*args, **kwargs)
                return ret
            else:
                login()
    return inner

def login():
    global flag
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "123456":
        flag = True
        print("登录成功")
    else:
        print("登录失败")

@login_verify
def add():
    print("执行添加操作")

@login_verify
def upd():
    print("执行更新操作")

# add()
# upd()
# add()
# upd()
# upd()

'''高阶装饰器，同一个函数被多个装饰器装饰，采用就近原则'''

def wrapper_1(fn):
    def inner(*args, **kwargs):
        print("wrapper_1_bagin")
        ret = fn(*args, **kwargs)
        print("wrapper_1_after")
        return ret
    return inner

def wrapper_2(fn):
    def inner(*args, **kwargs):
        print("wrapper_2_bagin")
        ret = fn(*args, **kwargs)
        print("wrapper_2_after")
        return ret
    return inner

def wrapper_3(fn):
    def inner(*args, **kwargs):
        print("wrapper_3_bagin")
        ret = fn(*args, **kwargs)
        print("wrapper_3_after")
        return ret
    return inner

@wrapper_3
@wrapper_2
@wrapper_1
def targets():
    print("target function")

targets()

'''
带参数的装饰器
把装饰器封装进函数，调用函数名
'''
def gua_outer(name):
    def gua(fn):
        def inner(*args, **kwargs):
            print(f"开启{name}外挂")
            ret = fn(*args, **kwargs)
            print(f"关闭{name}外挂")
            return ret
        return inner
    return gua

@gua_outer("饕餮")
def dnf():
    print("玩DNF")

@gua_outer("耄耋")
def lol():
    print("玩LOL")

dnf()
lol()