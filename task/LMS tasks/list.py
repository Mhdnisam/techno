# Given the list numbers = [5, 10, 15, 20, 25], perform the following operations: access and print the first and last elements, modify the second element to 12, add a new element 30 to the end of the list, and remove the third element. Print the final state of the list.

# printing first and last number
numbers = [5, 10, 15, 20, 25]
print("first number = ", numbers[0])
print("last number = ", numbers[-1])
# update 10 to 12
numbers[1] = 12
print(numbers)
# adding 30 to end of the list
numbers.append(30)
print(numbers)
# removing third elements
del numbers[2]
print(numbers)
# final state of list
print("final state =", numbers)