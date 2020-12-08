'''
    多态
'''


class H2O:

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def print_status(self):
        if self.temperature < 0:
            print('{}的温度于零摄氏度'.format(self.name))
        elif self.temperature > 0 and self.temperature < 100:
            print('{}的温度高于零度但小于一百摄氏度'.format(self.name))
        elif self.temperature >= 100:
            print('{}的温度高于一百摄氏度'.format(self.name))


'''
    子类继承父类 如果导入 abc模块可以定义成接口 从而使得子类必须实现父类方法
    父类要加上 metaclass=abc.ABCMeta @abc.abstractmethod
'''


class Water(H2O):
    pass


class Ice(H2O):
    pass


class Steam(H2O):
    pass


'''
    子类调用父类方法产生不同结果 =====>多态
'''

w = Water('水', 37.5)
w.print_status()

i = Ice('冰', -1)
i.print_status()

s = Steam('水蒸汽', 100)
s.print_status()
