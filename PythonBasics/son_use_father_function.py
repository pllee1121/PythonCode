'''
    子类调用父类方法
    vehicle 交通工具
'''


# class vehicle:

#     def __init__(self, city, vehicle_type, speed, load, power):
#         self.city = city
#         self.speed = speed
#         self.load = load
#         self.power = power
#         self.vehicle_type = vehicle_type

#     def print_info(self):
#         info = '所在城市'+self.city+'交通工具'+self.vehicle_type + \
#             '速度是'+self.speed+'动力来自'+self.power+'能容纳'+self.load+'人'
#         return info


# class subway(vehicle): # 子类继承父类交通工具对象 Vehicle
#     def __init__(self, country, city, vehicle_type, speed, load, power):

#         # 子类引用父类对象 可以减少代码的冗余
#         vehicle.__init__(self, city, vehicle_type, speed, load, power)
#         self.country = country

#     def print_info(self):
#         get = vehicle.print_info(self)
#         return '在'+self.country+get


# s1 = subway('China', '深圳', 'subway', '100km/h', '1000000', 'electric')
# print(s1.print_info())


# class vehicle:

#     def __init__(self, city, vehicle_type, speed, load, power):
#         self.city = city
#         self.speed = speed
#         self.load = load
#         self.power = power
#         self.vehicle_type = vehicle_type

#     def print_info(self):
#         info = '所在城市'+self.city+'交通工具'+self.vehicle_type + \
#             '速度是'+self.speed+'动力来自'+self.power+'能容纳'+self.load+'人'
#         return info


# class subway(vehicle):  # 子类继承父类交通工具对象 Vehicle
#     def __init__(self, country, city, vehicle_type, speed, load, power):

#         # 子类引用父类对象 可以减少代码的冗余
#         super().__init__(city, vehicle_type, speed, load, power)
#         self.country = country

#     def print_info(self):
#         get = super().print_info()
#         return '在'+self.country+get


# s1 = subway('China', '深圳', 'subway', '100km/h', '1000000', 'electric')
# print(s1.print_info())
