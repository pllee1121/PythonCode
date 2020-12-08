'''
    深度优先规则
    depth-first
'''

class A:
    def print_info(self):
        print('A')


class B(A):
    def print_info(self):
        print('B')


class C(A):
    def print_info(self):
        print('C')


class D(B):
    def print_info(self):
        print('D')


class E(C):
    def print_info(self):
        print('E')


class F(D,E):
    def print_info(self):
        print('F')

f = F()
f.print_info()
print(F.__mro__)