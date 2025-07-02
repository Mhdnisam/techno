class A:
    def funct1(self):
        print("hi")

    def funct2(self):
        print("hello")


class B(A):
    def funct1(self):
        print("nisam")

    def funct4(self):
        print("how are you")
        super().funct1()  # call parent class same funct


obj = B()
obj.funct2()
obj.funct1()
obj.funct4()
