class Func:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        # 自定义打印实例对象的返回值
        return '自定义的实例返回值是: '+'姓名是'+self.name+'年龄是' + str(self.age)


f = Func('李朋亮', 23)
print(f)  # print()函数本质上是执行 str(f) ----> f.__str__()

'''
    解释器执行 __repr__方法
'''

class Func:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):

        # 自定义打印实例对象的返回值
        return '姓名是'+self.name+'年龄是' + str(self.age)


f = Func('李朋亮', 23)
# print(f)  # print()函数本质上是执行 str(f) ----> f.__str__()
print(f)