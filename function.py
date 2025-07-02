def function():
 x = 10
 print(x)
function()


x = 30
def function1():
    print(x)
function1()


#

def function():
    print("hi my world")


function()


def myfunction(name):
    print("my names is", name)


myfunction("nisam")


def mfunction(name, age, place):
    print("hi iam ", name + "\nmy age is", str(age) + "\ni am coming from", place)


mfunction("nisam", 21, "vanimel")

# task
# calculator

a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = str(input("select the operator(+, -, *, /) = "))
def addition():
 if c == '+':
    print("addition =", a + b)
addition()

def substraction():
 if c == '-':
    print("substraction =", a - b)
substraction()

def division():
 if c == '/':
    print("division =", a / b)
division()

def mul():
 if c == '*':
    print("mul =", a * b)
mul()
