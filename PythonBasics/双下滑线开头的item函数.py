'''
    __getitem__
    __setitem__
    __delitem__
'''


class Item:

    def __init__(self, name):
        self.name = name

    def __getitem__(self, key):
        print('--->执行getitem')
        return self.__dict__[key]

    def __setitem__(self, key, value):
        print('---->执行setitem方法')
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('--->执行delitem')
        self.__dict__.pop(key)


i = Item('李朋亮')
print(i.__dict__)

i['age']=23
i['school']='宿州学院'
print(i.__dict__)

print(i['name'])

del i['name']
print(i.__dict__)