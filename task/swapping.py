a = 10
b = 32
a, b = b, a
print("before swapping a =", b)
print("before swapping b =", a)
print("\nafter swapping a =", a)
print("after swapping b =", b)

# using three variables
print("\nusing three variables")
a = 10
b = 32
c = a
a = b
b = c
print("\nbefore swapping a =", c)
print("before swapping b =", a)
print("\nafter swapping a =", a)
print("after swapping b =", c)

