# count = 0
# while count < 3:
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#     if username == 'pllee'and password == '12345':
#         print("登陆成功")
#         break
#     elif:
#         count += 1
#         print("用户名或密码错误请重新登陆")
# a = 'pLLee'
# print(a.__index__)
# r = a.casefold()
# t = r.center(20,"-")
# print(t)

# n = a.count('e',3,4)
# print(n)

# message = "I'am {}, age is {}".format('pllee', 22)
# print(message)

# split()函数对字符串进行分割
# string = "5+9"
# s1, s2 = string.split("+")
# n1 =eval(s1)
# n2 =eval(s2)
# print(s1, s2, n1+n2)

# lis = ['hello','good','create']
# s = ''
# for l in lis:
#     s += l

# for i in s:
#     print(i)

# s = "+".join(lis)
# print(s)


# t = (1,2,3,[(2,3)],11,22)
# t[3][0][0] = 1
# print(t)

# 字典

# v = dict.fromkeys(['k1','k2','k3'],1)
# print(v)
# print(type(v['k1']))
# v1 = v.get('k1')
# print(v1)

# v = {'k1':'value1','k2':'value2'}
# print(v.get('k1'))


# 集合

# p_stu = ['lpl','lg','lg','nyw','gjm']
# l_stu = ['lpl','lg','nyw','wjq']

# sp_stu =set(p_stu)
# sl_stu = set(l_stu)

# sl_stu.update([1,2])
# print(sl_stu)
# together = sp_stu.intersection(sl_stu)
# dif = sp_stu.difference(sl_stu)
# bingj = sp_stu.union(sl_stu)
# print(bingj)
# print(dif)
# print(together)

# msg = 'I am %(name)s age is %(age)d' % {'name': 'pllee', 'age': 22}
# print(msg)

# msg1 = 'I am {name} age is {age:.2f}'.format(name='pllee', age=22.222)
# print(msg1)

# print('pllee','lpl',0,0,sep=':')

# a = [1, 2, 3, None, (), [], ]

# print(len(a))

# name = 'pllee'
# def p():
#     print('p')

# def t():
#     print('t')
#     return p

# t()()

# def f1():
#     name = 'hello'

#     def f2():
#         print('nihao')

#     def f3():
#         print('gundan')
#     return f3


# f1()()

# 匿名函数

# func = lambda x:x**2
# print(func(10))
# name = 'lg'


# def f(x): return x+"_sb"


# print(f(name))

# def f(n):
#     print(n)


# def b(name):
#     print('my name is {}'.format(name))


# f(b())


# # 高阶函数 1. 函数接收的参数是一个函数名  2. 函数的返回值中包含函数
# def bar():
#     print('from bar')


# def foo():
#     print('from foo')
#     return foo

# a = foo()
# a()

# def test():
#     print('test')
#     test()

# test()

# num_l = [1, 2, 3, 4, 10, 9]

# def add_one(x):
#     return x+1

# def reduce_one(x):
#     return x-1

# def p(x):
#     return x**2

# def map_test(func, l):
'''
     测试自定义map函数
'''
#     after_l = []
#     for i in l:
#         res = func(i)
#         after_l.append(res)
#     return after_l

# # 使用 lambda 函数替代自定义函数
# print(map_test(add_one, num_l))
# print(map_test(lambda x: x+1, num_l))

'''
 使用 lambda 函数替代自定义函数
'''

# print(map_test(reduce_one, num_l))
# print(map_test(lambda x: x-1, num_l))

# # 使用 lambda 函数替代自定义函数
# print(map_test(p, num_l))
# print(map_test(lambda x: x**2, num_l))

# # map方法的使用 map(方法,可迭代对象)
# map()'

'''
filter 函数的使用
'''

# movie_people = ['sb_lg','sb_gjm','sb_nwy','lpl','sb_wjq','zm']

# res = []
# for i in movie_people:
#     if not i.startswith('sb'):
#         res.append(i)

# print(res)

# movie_people = ['sb_lg', 'sb_gjm', 'sb_nwy', 'lpl', 'sb_wjq', 'zm']

# def funcs(i):
#     return i.startswith('sb')

# def funce(i):
#     return i.endswith('sb')

'''
 过滤器函数 传入函数和可叠戴对象
'''

# def filter_test(function,array):
#     res = []
#     for i in array:
#         if not function(i):
#             res.append(i)
#     return res

# a = filter_test(funcs,movie_people)
# b = filter_test(funce,movie_people)

# print(a)
# print(b)

# people = [{'name': 'pllee', 'age': 22},
#           {'name': 'gjm', 'age': 20},
#           {'name': 'lg', 'age': 21}
#           ]

# after_people = list(filter(lambda p: p['age'] <= 21, people))
# print()
# print(after_people)


# num = list(filter(lambda x: x % 2 == 0, range(101)))
# print(num)

'''
 reduce函数是把他们合并成一个对象
'''

# from functools import reduce

# num = reduce(lambda x,y: x+y,['l','p','p','ldsafj','sdaijf'],'a')
# print(num)


'''
内置函数
'''
# print(all([0, 1]))

# print(bool(None))
# print(bool(1))
# encode = bytes('你好', encoding='utf8')
# print(encode)
# print(encode.decode('utf8'))
# a = b'\xe4\xbd\xa0\xe5\xa5\xbd'
# print(a.decode())

# num = '12345'
# print(hash(num))
# print(hash(num))

# num = '123456'
# print(hash(num))

# print(help(dict))


# print('十进制转二进制 ' + bin(10))
# print('十进制转十六进制 ' + hex(10))
# print('十进制转八进制 ' + oct(10))

# print(__file__)
# print(globals())
# print(__doc__)

# list=list(zip(('1','2','3'),('a','b','c')))
# print(list)
# for l in list:
#     print(l)


# k_v ={'name':'pllee','age':22,'gender':'male'}
# a = list(zip(k_v.keys(),k_v.values()))
# print(a)
# keys = k_v.keys()
# values = k_v.values()
# print(list(keys))
# print(list(values))
# l = list(zip((keys),(values)))
# print(l)

# ll = {
#     'pllee':22,
#     'gjm':21,
#     'lg':21
# }
# print(sorted(zip(ll.values(),ll.keys()))) 
# def test():
#     msg = 'sdjfoa;jdjfoisj'
#     print(locals())
#     print(vars())
