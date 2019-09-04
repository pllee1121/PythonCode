# i = __import__('exerciselogin')
# i.test()

# f = open('PythonBasics/a', encoding='utf-8')
# print('-'*20)
# for i in range(6):
#     data = f.readline()
#     print(data)

# with open('a', 'r', encoding='utf-8') as a, \
#         open('b', 'w', encoding='utf8') as b:
#     data = a.read()
#     return_info = b.write(data)
#     if return_info:
#         print('写入成功')


# f = open('a','rb')
# data = f.read()
# print(f.encoding)
# print(f.readlines ())
# print(f.tell())
# ll = list(data)
# print(data[-1].decode('utf8') )

# f.seek(3)
# print(f.readline())
# import os
# path = os.getcwd()
# print(path)

# s = 'hello'
# iter_test = s.__iter__()
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())


# # for循环使用的是迭代器

# for i in s:         # s 这一步实际上是执行了迭代器协议转换成了可迭代对象  i_s = s.__iter__() 生成了一个可迭代对象 下一步是 i_s.__next__()
#     print(i)

# s = 'hello'
# i_s = s.__iter__()
# while True:
#     try:
#         print(i_s.__next__())   # 等价于 next(i_s)  内置函数
#     except StopIteration:
#         print('迭代完毕, 循环终止')
#         break

# import time
# s_t = time.time()
# print(sum([i for i in range(100000000)]))
# e_t = time.time()
# print('一效率低费内存: '+str(e_t-s_t)+'秒')

# s_t = time.time()
# print(sum(i for i in range(100000000)))
# e_t = time.time()
# print('二效率高省内存: '+str(e_t-s_t)+'秒')


# 生成器基于迭代器
# def test():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# res = test()
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


# 生成器的好处 1、减少占用内存空间（不需要开辟额外的空间用来存储） 2、执行效率高

# 对比 1
# def prodect_baozi_slow():
#     l = []
#     for i in range(1,11):
#         l.append('做好的第{}屉包子'.format(i))
#     return l
# res = prodect_baozi_slow()
# print(res)

# 2
# def prodect_baozi():
#     for i in range(1,11):
#         print('可以出售: ')
#         yield '做好的第{}屉包子'.format(i)


# res = prodect_baozi()
# print('\t顾客来买'+res.__next__())
# print('\t顾客来买'+res.__next__())
# print('\t顾客来买'+res.__next__())
# print('\t顾客来买'+res.__next__())

# l1 =[11,22,33]
# l2 = [33,44,55]
# print(set(l1) & set(l2))

# def fun(x,*z,**y):
#     print(x,y,z)

# fun(1,2,3)

# s = "中文"
# print(s.encode('utf8'))
# print(bytes(s,'utf8'))

# import time

# # 时间戳
# print(time.time())

# # 打印当前结构化时间
# print(time.localtime())

# # 打印格林威治时间
# print(time.gmtime())

# # 结构化时间转时间戳
# print(time.mktime(time.localtime()))

# # 结构化时间转换成字符串时间
# print(time.strftime("%Y-%m-%d %X", time.localtime()))

# # 字符串时间转换为结构化时间
# print(time.strptime("2019-8-8 18:30:34", "%Y-%m-%d %X"))

# # 不需自定义时间显示格式 直接使用
# print(time.asctime())  # 时间戳转换成字符串时间
# print(time.ctime())   # 结构化时间转换成字符串时间

# import datetime

# print(datetime.datetime.now())

# import random

# # choice 方法随机选取列表中的一个值
# print(random.choice([1,2,3,4,5,6,7]))

# # sample 方法随机选取给定列表的给定的 n 个数
# print(random.sample([2,4,6,8],3))

# # randint 方法随机选取给定范围中的一个值, 两边的值都能取到 左闭右闭
# print(random.randint(2,3))

# # randrange 方法随机选取给定范围的一个值, 取不到右侧的值 左闭右开
# print(random.randrange(2,3))

# # 随机选取给定范围中的浮点数
# print(random.uniform(1,2))

# # 随机选取 [0,1) 中的浮点数
# print(random.random())


# '''
#     验证码选取
# '''

# import random


# def d_code():

#     ret = ''
#     for i in range(5):
#         num = random.randint(0, 9)
#         lowS = chr(random.randint(65, 90))
#         upS = chr(random.randint(96, 122))
# s = str(random.choice([lowS, upS]))
#         string = str(random.choice([num, s]))
#         ret += string
#     return ret


# print(d_code())


# import os

# print(os.system('dir'))
# print(os.environ)
# a,b = os.path.split('/Users/pllee/VSCode/PythonCode/PythonBasics/fileoperate.py')
# print(type(os.path.split('/Users/pllee/VSCode/PythonCode/PythonBasics/fileoperate.py')))
# print(a)
# print(b)
# print(os.path.dirname()

# print(os.path.split(r'/Users/pllee/VSCode/PythonCode/PythonBasics/fileoperate.py'))
# print(os.path.dirname(r'/Users/pllee/VSCode/PythonCode/PythonBasics/fileoperate.py'))
# print(os.path.basename(r'/Users/pllee/VSCode/PythonCode/PythonBasics/fileoperate.py'))


# 路径拼接

# a = '/Users/pllee/VSCode/PythonCode/PythonBasics/'
# b = 'fileoperate.py'
# c = os.path.join(a, b)
# d = a + b
# print(c)
# print(d)
# print(os.path.abspath('1.py'))

# os.system('ls /Users/pllee/Movies')


# '''
#     sys模块的部分功能使用
# '''
# import sys
# print(sys.path)
# print(sys.platform)

# import sys
# import time

# for i in range(100):
#     sys.stdout.write('#')
#     time.sleep(0.05)
#     sys.stdout.flush()
#     while i==99:
#         print('100%')
#         break
# print()

# import json

# s = 'hello'
# j = json.dumps(s)
# print(j)
# print(type(j))


# '''
#     json 转换的数据类型为字符串(str)
# '''
# import json

# with open("json_test", 'r') as f:
#     data = f.read()
#     print(type(data))
#     dic = json.loads(data)
#     print(dic['name'])

# '''
#     pickle 转换的数据类型为字节(bytes) 读写都需要加 b , pickle需求较小常使用 json 模块
# '''
# import pickle


# '''
#     以下注释代码为创建写入数据
# '''
# data = {'name': 'pllee', 'age': 22}
# pic = pickle.dumps(data)

# with open('pickle_text', 'wb') as p:
#     p.write(pic)

# '''
#     以下代码为使用 pickle 模块读取数据代码
# '''
# with open('pickle_text','rb') as p:
#     data=p.read()
#     print(type(data))
#     pic_text=pickle.loads(data)
#     print(pic_text)


'''
    shelve模块
'''

import shelve

f = shelve.open(r'shelve_test')

# f['stu1'] = {'name':'pllee','age':22}
# f['stu2'] = {'name':'lipengliang','age':20}
# f.close() 

print(f.get('stu2')['age'])