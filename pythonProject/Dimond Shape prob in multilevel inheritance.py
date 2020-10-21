class A:
    def meth(self):
        print('this is a method from class a ')
class B(A):
    def meth(self):
        print('this is a method from class b')
class C(A):
    def meth(self):
        print('this is a method from class c')
class D(C,B):
    pass
    # def meth(self):
    #     print('this is a method from class d')

a = A()
b = B()
c = C()
d = D()

print(d.meth())