'''
    reflect 反射
    python 自带的四个函数的使用
    hasattr(对象,'属性或方法') 判断实例是否存在
    getattr(对象,'属性或方法',default=None) 获取属性或方法的地址
    setattr(对象,属性或方法) 给实例怎加属性或方法
    delattr(对象,属性) 删除实例中的属性
'''


class BlackMedium:

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_hourse(self):
        print('{}正在卖房子'.format(self.name))

    def rent_hourse(self):
        print('{}正在租房子地址在{}'.format(self.name, self.addr))


custom = BlackMedium('李钢', '合肥')
print(hasattr(custom, 'name'))

get = getattr(custom, 'addr')
print(get)

'''
    第三个参数 default 自定义可以在查找不到该属性的时候不报错
'''
get = getattr(custom, 'addd', '没有该属性')
print(get)


'''
    给属性设置对象
'''

setattr(custom,'city','深圳')
print(custom.__dict__)

# 往 custom 对象里面传入函数
setattr(custom,'func',lambda self: self.name+'love love love')
print(custom.__dict__)
print(custom.func(custom))

'''
    删除对象的属性
'''

delattr(custom,'name')
print(custom.__dict__)
