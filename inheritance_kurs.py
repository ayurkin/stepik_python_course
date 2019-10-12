# class A1:
#    def foo(self):
#       print("A1")
#
# class A2:
#    def foo(self):
#       print("A2")
#
# class B(A1):
#    pass
#
# class C(A2):
#    def foo(self):
#       print("C")
#
# class D:
#    def foo(self):
#       print("D")
#
# class E(B, C, D):
#    pass
#
# E().foo()
# print(E.mro())

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass

print(E.mro())