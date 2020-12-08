class Func:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __format__(self, format_spec):
    #     return '{0}{0}'.format(self.name,self.age)


f = Func('李朋亮','23')
f.__format__()