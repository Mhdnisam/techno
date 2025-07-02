fruits = ["apple", "banana", "cherry", "mango"]
newlist = []
for x in fruits:
 if "a" in x:
    newlist.append(x)
print(newlist)

# using list comprehension
fruits = ["apple", "banana", "cherry", "mango", "pine apple"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
