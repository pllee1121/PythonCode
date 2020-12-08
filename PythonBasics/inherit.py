# '''
#     继承 inherit
# '''


# class Parents:
#     name = 'lg'

#     def __init__(self, name):
#         print(name)

#     def print_info(self):
#         print('来自父类的信息')


# class Son(Parents):
#     '''
#         子类继承父类
#     '''

#     def __init__(self, name):
#         print('子类信息', name)

#     def print_info(self):
#         print('子类输出的信息')


# s = Son('lg')
# s.print_info()
# print(Parents.__dict__)
# print(Son.__dict__)

'''
    使用 @abc.abstractmethod装饰器 可以对子类限制, 使得子类必须实现父类方法
    想当于 Java 语言中的接口
'''
import abc


class Disk(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Memory(Disk):
    def read(self):
        print('memory read')

    def write(self):
        print('memory write')


class Cdrom(Disk):

    def read(self):
        print('cdrom read')

    def write(self):
        print('cdrom write')


m = Memory()
m.read()
