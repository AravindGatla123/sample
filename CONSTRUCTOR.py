class A:

    def __int__(self):
        print("Print A init")

    def feature1(self):
        print("Feature 1-a is working")




class B:

    def __int__(self):
        print("Print B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A,B):

    def __init__(self):
        super().__init__()
        print("init of c")

    def feat(self):
        super().feature1()

b1 = A()
c1 = B()
a1 = C()
a1.feat()

