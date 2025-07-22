# print("hello")
# print("hello", "saliha")
# print("price :", 3032)
#
# my_int = 1
# print(my_int)
# my_int = 5
# print(my_int)
#
# a = 3
# b = 4
# c = a == b
# d = a >= b
# e = a != b
# f = a <= b
# print(c, d, e, f)

# list = [1, 2, 3, 4, 5, 6]
# for i in list:
#     if i % 2 == 0:
#         print("even number is :", i)
#
# # factorial
# num = int(input("enter a number : "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

# count 1 to 5

# count = 1
# while count <= 5:
#     print("hello world")
#     count += 1

# count 5 to 1
# i = 5
# while i >= 1:
#     print(i)
#     i += -1


# # 5 multiplication
# i = 5
# while i <= 10:
#     print(i)
#     i += 5
# another way
# i = 1
# while i <= 5:
#     print(i*5)
#     i += 1

# user input to find the multiples
# n = int(input("enter a number"))
# i = 1
# while i <= n:
#     print(i*5)
#     i += 1


# fibbinoci
# n = int(input("enter a number"))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b

# find the prime number

# n = int(input("enter the number"))
# if n <= 1:
#     print("not prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("it is not a prim number")
#             break
#     else:
#         print("it is a prime number")

# iterating number
# for i in range(10, 0, -2):
#     print(i)

# odd and even

# a = int(input("enter a number"))
# if a % 2 == 0:
#     print("this is a even number")
# else:
#     print("it is a odd number")

# print 1 to 10

# for i in range(1, 11):
#     print(i)

# multiplication table

# n = int(input("enter a number"))
# for i in range(1, 11):
#     print(f"{i} * {n}=", i * n)
#

# using while loop

# n = int(int(input("enter a number")))
# i = 1
# while i <= n:
#     print(i * n)
#     i = i + 1

# # 1 to 100
# i = 3
# while i <= 100:
#     print(i)
#     i = i + 3
#

# # factorial
# i = int(input("enter a number"))
# fact = 1
# while i > 0:
#     fact = fact * i
#     i = i - 1
# print("factorial of this number:", fact)


# odd or even
# n = int(input("enter the range"))
# while n % 2 == 0:
#     print("it is a even number")
# else:
#     print("it is a odd number")
#     n = n + 1

# # finding odd or even sum
# i = 1
# sum = 0
# while i <= 10:
#     if i % 2 == 1:
#         sum = sum + i
#     i = i + 1
# print(sum)
#
# pattern nested loop
# j = 1
# while j <= 5:
#     i = 1
#     while i <= j:
#         print("*", end="")
#         i = i + 1
#     print("\n")
#     j = j + 1

# list

# l = [1, 2, 3, 4, " nisam"]
# print(l)
# print(l[0:4])
# print(l[:5])
# l[0] = 30
# print(l)
# print(l[-1])

# list = [0, 0, 0, 0, 0]
# i = 0
# while i <= 4:
#     list[i] = int(input("enter a number"))
#     i = i + 1
# print(list)
# i = 0
# while i <= 4:
#     print(list[i])
#     i = i + 1
#
#
# list = [10, 12, 38, 384]
# list2 = [20, 32, 30, 39]
# list.insert(1, 20)
# list.append(28)
# list.extend([25, 67])
# list[0] = 15  # update
# x = len(list)  # find the length
# list.extend(list2)  # add two list
# list.remove(39)  # removing a element
# list.pop(3)   # pop using specific elements
# # list.clear()  # clearing all the elements
# del.list[0]
# print(list)
# print(x)

# list = [1, 2, 3, "nisam"]
# list[0] = 30
# list.append("saliha")
# list.extend([32, 30])
# list.insert(0, 62)
# list.remove(62)
# list.pop(2)
# del list[1]
# print(list)

# math  build in key word
# int = [1, 34, 54, 3, 4, 5]
# print("largest number = ", max(int))
# x = abs(-329)
# print(x)
# x = pow(3, 4)
# print(x)
# import math
# x = math.sqrt(5)
# y = math.ceil(1.5)
# x = math.floor(3.4)
# print(x, y)
# x = math.pi
# print(x)

# tuple

