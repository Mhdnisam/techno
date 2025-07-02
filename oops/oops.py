class Cars:

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def show_details(self):
        print(f"name: {self.name}, color: {self.color}, year: {self.year}")


obj2 = Cars('breeza', 'red', 2019)
obj2.show_details()

# inheritence


class Animal:

    def fox(self, fname):
        print(fname)


class Dog(Animal):

    def bark(self):
        print("i am hungry")


obj1 = Dog()
obj1.fox("nisam")
obj1.bark()



