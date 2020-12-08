# '''
#     packaging 封装
# '''


# class Package:
#     '''
#         在属性前面加上 _ __ 使得该属性成为私有属性 外部无法调用
#         但是在 python 中依然能够获取到属性值
#     '''

#     _country = 'China'
#     __university = 'SuZhouUniversity'

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def print_message(self):
#         print(self.name, self.age, self.salary)


# p = Package('李朋亮', '22', '10000')
# p.print_message()

# print(p._country)
# print(Package.__dict__, '\n')
# # print(p.__university) 这样调用类的属性是无法获取的
# print(p._Package__university)


'''
    真正意义上的封装 是内部为外部提供接口来实现外部使用对内部的私有属性调用
'''


class Room:

    def __init__(self, owner, length, width, height):

        self.owner = owner
        self.__length = length
        self.__width = width
        self.__heigth = height

    ''' 
        内部定义接口给外部调用
    '''
    def room_area(self):
        print('房屋面积是', self.__length*self.__width, '平方米')


r = Room('李钢', 100, 100, 100)
r.room_area()
