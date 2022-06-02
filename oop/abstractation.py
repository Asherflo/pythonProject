import abc

class A:
    __metaclass__ =abc.ABCmeta


class B(A):
    def must_be_implement(self):
        print("hello")
