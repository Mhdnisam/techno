from abc import ABC,abstractmethod

class Animel(ABC):
    @abstractmethod
    def animal_details(self):
        pass

class Dog(Animel):

    def animal_details(self, name, color, price):
        print("Dog name =", name)
        print("color =", color)
        print("price =", price)

class Cat(Animel):

    def animal_details(self, name, color, price):
        print("Cat name =", name)
        print("color =", color)
        print("price =", price)

class Bird(Animel):

    def animal_details(self, name, color, price):
        print("Bird name =", name)
        print("color =", color)
        print("price =", price)



dog = Dog()
dog.animal_details("huskey", "white", 45000)
cat = Cat()
print()
cat.animal_details("persion", "brown", 25000)
print()
bird = Bird()
bird.animal_details("parrot", "green", 35000)
