# initialize a dictionary with key-value pairs and perform operations including accessing a value using a key,
# adding a new key-value pair, modifying an existing value,
# and removing a key-value pair. Print the resulting dictionary.

dict1 = {"name": "saliha", "age": 28, "place": "nadapuram"}
# accessing a value using a key
print("student name =", dict1["name"])
# add a new key valuie pair
dict1["hobby"] = "eating"
print(dict1)
# modifying an existing value
dict1["age"] = 22
print("updated age =", dict1)
# removing a key-value pair
del dict1["age"]
print(dict1)
# Print the resulting dictionary
print("final result =", dict1)