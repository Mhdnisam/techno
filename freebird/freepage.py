# arithemetic operator
#
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# print("addition =", a + b)
# print("subtraction =", a - b)
# print("division =", a / b)
# print("mul = ", a * b)
# print("modulus =", a % b)
# print("floor division", a // b)
# print("exponentiation = ", a ** b)
#
# comparison operator
# if both values are same
#
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# if a == b:
#     print("true")
# else:
#     print("false")
#
# if one number is greater
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# if a > b:
#     print("a is greater")
# elif b > a:
#     print("b is greater")
# else:
#     print("both number a equal")
#
# if  a number is smaller
#
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# if a < b:
#     print("a is smaller")
# elif b < a:
#     print("b is smaller")
# else:
#     print("both are equal")
#
# if two number are not  equal
#
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# if a == b:
#     print("both are rqual")
# else:
#     print("not equal")
#
# # person passed
# a = int(input("enter a number"))
# if a <= 33:
#     print("true")
# else:
#     print("false")
#
# # logical operator
#
# and operator(Check if a number is greater)
#
# a = 10
# b = 5
# if b >= 5 and a <= 10:
#     print("true")
# else:
#     print("false")
#
#
# or operator(Check if a number is less than 3 or greater than 10)
# a = 12
# b = 5
# if a <= 3 or a >= 10:
#     print("true")
# else:
#     print("false")
#
#
# # not operator(Operator  Set x = True and print not x.)
# a = 10
# b = 45
# print(not a > b)
#
# x = True
# print("x =", not x)
#
#
# combine conditions(Write a program to check if a person is above 18 and has an ID card.)
# name = input("enter your name")
# age = int(input("enter your age"))
# place = input("enter your place")
#     if age <= 18:
#         print("doesn't create you id card")
#
#
# logical operator
#
# username = input("enter your username")
# password = int(input("enter yout password"))
# if password == 1234:
#     print("access granded")
# else:
#     print("access denied")
#
# Determine whether a number is between 1 and 100 or divisible by 5.

# a = int(input("enter a number between 1 - 100 :"))
# if (a >= 1 and a <= 100) or (a % 5 == 0):
#     print("the number is between 1 -100,it is divisible by 5")
# else:
#     print("the number is not between 1 -100,not divisible")

# Write a login simulation: if username is correct and password is correct → success.
#
# c_username = "nisam"
# c_password = 1234
# username = input("enter you username:")
# password = int(input("enter your password:"))
# if username == c_username and password == c_password :
#     print("success")
# else:
#     print("denied")

# # assignment operator
#
# x = 10
# print(x)
# x += 5
# print(x)
# x -= 2
# print(x)
# x *= 3
# print(x)
# x = 12
# x /= 5
# print(x)
# x =12
# x //= 5
# print(x)
# x =12
# x %= 5
# print(x)

# Create a counter that increases by 2 in each step using +=.
# counter = 2
# while counter <= 10:
#     print("counter = ", counter)
#     counter += 2


# Calculate a power of a number using **= instead of **.
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# a **= b
# print(a)

# # membership operator
# fruits = ['banana', 'apple', 'cherry']
# print('banana' in fruits)
# print("grape" not in fruits)
# print("grape"  in fruits)
#
# number = [1, 2, 3, 4, 5, 6]
# if 9 in number:
#     print("4 is there in the list")
# else:
#     print("no this number is not in list")


# identity operator

x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is not y)
print(x is z)
print(x == z)
