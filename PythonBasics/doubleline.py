'''
    双下划线开始并结尾的方法的使用
    以下三个函数系统默认提供 自定义
    的话会覆盖调系统提供的
'''


class func:

    def __init__(self, name):
        self.name = name


    def __getattr__(self, item):
        print('执行__getattr__方法')

    def __delattr__(self, item):
        print('正在执行__delattr__方法')
        self.__dict__.pop(item)

    def __setattr__(self, key, value):
        print('正在执行__setattr__方法')
        '''
            如果使用 self.key = value 
            将会进入无限递归
        '''
        self.__dict__[key] = value


f = func('李朋亮')
'''
    测试__getattr__()方法
'''
print(f.name)
print(getattr(f, 'name'))
f.addr  # 在调用对象 f 中不存在的属性时会自动触发 __getattr__() 方法的执行
print('*'*20)

'''
    测试__delattr__()方法
'''
del f.name  # 在删除对象中的属性的时会自动触发 __delattr__() 方法的执行
print(f.name)
print('*'*20)

'''
    测试__setattr__()方法
'''
print(f.__dict__)
f.z = 2
print(f.__dict__)
