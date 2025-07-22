fruits = ["apple", "banana", "cherry"]
fruits_tuple = ("apple", "banana", "cherry")
# modified second element in list
fruits[1] = "blueberry"
print(fruits)
# modified second element in tuple
try:
    fruits_tuple[1] = "blueberry"
    print(fruits_tuple)
except:
    print("error occured while modifying in tuple")
