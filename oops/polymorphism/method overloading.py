class A:
    def find_sum(self, a, b):
        print(a + b)

    def find_sum(self, a, b, c=0):
        if c == 0:
            print(a + b)
        else:
            print(a + b + c)

obj = A()
obj.find_sum(1, 5)
obj.find_sum(1, 2, 6)
