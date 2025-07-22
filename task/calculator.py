a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
print("select the operator:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floordivision\n6.Modulus")
c = int(input("enter the operator"))
if c == 1:
    result = a + b
    print("answer=", result)
elif c == 2:
    result = a - b
    print("answer=", result)
elif c == 3:
    result = a * b
    print("answer=", result)
elif c == 4:
    if b == 0:
        print("zero division not possible")
    else:
        result = a / b
        print("answer=", result)
elif c == 5:
    if b == 0:
        print("zero division not possible")
    else:
        result = a // b
        print("answer=", result)
elif c == 6:
    result = a % b
    print("answer=", result)
else:
    print("wrong selection")
