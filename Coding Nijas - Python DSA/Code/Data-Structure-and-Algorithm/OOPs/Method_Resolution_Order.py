class B:
    pass


class A(B):
    pass


class C(A, B):
    pass


class D(C, A):
    pass


print(D.mro())
