
# class Dog:

#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def play(self):
#         print('{}正在打篮球'.format(self.name))

#     def sing(self):
#         print('虽然{}年纪已经达到了{} 正在唱歌'.format(self.name, self.age))


# d = Dog('李钢', '22', '男')
# d.play()
# d.sing()


# class Test:
#     '''创建每一个对象时都会自动执行__init__()函数'''

#     def __init__(self, name, age, gender):
#         self.xingming = name
#         self.nianling = age
#         self.xingbie = gender

#     def printinfo(self):
#         print('我的名字是{}今年{}岁'.format(self.xingbie, self.nianling))

#     def printsex(self):
#         ''' 如果不含有self参数的话, 对象实例调用会出错
#             TypeError: printsex() takes 0 positional arguments but 1 was given
#         '''
#         print('我的性别是{}'.format(self.xingbie))


# t = Test('李朋亮', '23', '男')
# print('创建的实例产生的字典包含的数据', t.__dict__)  # 打印创建的对象数据
# print('类中包含的数据和方法', Test.__dict__)  # 打印类中包含的数据和方法

# '''在定义的函数中需要含有self参数,因为当创建对象调用自定义函数时
#    会主动想其中传入创建的对象。因此需要self参数
#    self 本身就相当于实例本身
# '''

# print('\n<', '-'*20, '>调用类中的方法')
# t.printinfo()
# t.printsex()

# class Chinese:

#     speak_language = 'chinese'

#     def __init__(self, name, age, sex):
#         self.xingming = name
#         self.nianling = age
#         self.xingbie = sex
#         self.speak()

#     def speak(self):
#         print('{}说着{}'.format(self.xingming, self.speak_language))

#     def print_age(self, age):
#         print('{}今年」{}岁'.format(self.xingming, age))


# # 查看
# print(Chinese.speak_language)
# person = Chinese('李朋亮','22','男')
# print(person.speak_language)
# # 增加
# Chinese.country='China'
# print(Chinese.country)
# print(person.country)

# # 删除
# del Chinese.speak_language
# try:
#     print(Chinese.speak_language)
# except:
#     print('该属性不存在')

# # 改
# print(Chinese.__dict__)
# Chinese.country='America'
# print(Chinese.__dict__)

# '''
#     对于没有指明类或实例的情况下调用的数据说明
# '''
# country = '日本'


# class Test:

#     country = '中国'

#     def __init__(self, name):
#         self.name = name
#         print('国家:', country)

#     def print_name(self):
#         print('my name is {}'.format(self.name))


# '''
#     此时为何打印的 country 为日本, 因为想要打印类里面的 country 值需要调用类或者实例才能打印其值
# '''
# t = Test('李朋亮')

# '''
#     以下两种情况打印的 country 值均为类中的 country 值中国🇨🇳
# '''
# print('类调用的country值:', Test.country)
# print('实例调用的country值:', t.country)


# '''
#     静态属性
# '''


# class Room:

#     tag = '我是变量tag'

#     def __init__(self, name, length, width, height):
#         self.name = name
#         self.length = length
#         self.width = width
#         self.height = height

#     @property  # 属性
#     def house_owner(self):
#         print('房屋的主人是:{}'.format(self.name))

#     @property
#     def house_area(self):  # 计算房屋面积 使用 print 直接打印
#         print('房屋的占地面积是{}平方米'.format(self.length*self.width))

#     @property
#     def house_volume(self):  # 计算房屋体积 使用 return 返回值需要有参数用来接收
#         return '房屋的体积是'+str(self.length*self.width*self.height)+'立方米'

#     @classmethod  # 类方法 可以不需要创建实例类就能够调用的方法
#     def class_info(cls, x):
#         print('-'*20)
#         print(cls)
#         print(cls.tag, x)

#     @staticmethod
#     def static_method(x, y, z):  # 静态方法 是类的工具包 不需要传入指定类或实例
#         print('传入的数据是{}{}{}'.format(x, y, z))

#     def no_static_tag(x, y, z):
#         print('使用no static tag方法传入的数据是{}{}{}'.format(x, y, z))


# r = Room('李朋亮', 10, 15, 4)
# print(r.name)
# r.house_area
# print(r.house_volume)

# Room.class_info('来自类调用的方法')
# print('-'*20)
# Room.static_method('李朋亮', '李钢', '哥哥')
# r.static_method('小狗', '小猫', '屎')

# print('-'*20+'无静态方法标记的函数使用')
# Room.no_static_tag('李', '葛', '吴')

# '''
#     对于非静态方法的调用, 实例对象会传入实例对象从而导致错误 如下
#     no_static_tag() takes 3 positional arguments but 4 were given

#     此调用无法执行 r.no_static_tag('吴亦凡','鹿晗','关晓彤')

# '''


'''
    类的组合
'''


# class School:
#     '''
#         定义学校类
#     '''

#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr


# class Course:

#     def __init__(self, course_name, course_price, course_num, school):
#         self.course_name = course_name
#         self.course_price = course_price
#         self.course_num = course_num
#         self.school = school


# s = School('宿州学院', '皖宿州市埇桥区')

# course = Course('python', '500', '001', s)
# print(course.__dict__)
# print(course.school.name)


class School:

    def __init__(self, school_name, school_addr, school_type):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_type = school_type

    def print_info(self):
        info = '学校名字是'+self.school_name+'地址位于' + \
            self.school_addr+'是一所'+self.school_type
        print(info)


class Teacher:

    def __init__(self, teacher_name, teacher_age, teacher_course, school):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.teacher_course = teacher_course
        self.school = school

    def teacher_info(self):
        info = '姓名'+self.teacher_name+'年龄为'+self.teacher_age + \
            '是一名'+self.teacher_course+'老师'+'任职于'+self.school.school_type
        print(info)


class Course:

    def __init__(self, course_name, course_price, course_num, teacher):
        self.course_name = course_name
        self.course_price = course_price
        self.course_num = course_num
        self.teacher = teacher

    def course_info(self):
        info = '课程名是'+self.course_name+'课程价格为'+self.course_price + \
            '课程编号为'+self.course_num+'带课老师是'+self.teacher
        print(info)


s1 = School('宿州学院', '皖宿州市埇桥区', '大学')
s1.print_info()

t1 = Teacher('张光辉', '30', '高等数学', s1)
t1.teacher_info()

c1 = Course(t1.teacher_course, '500', '001', t1.teacher_name)
c1.course_info()
