# open and write  file

file = open('file.txt', 'w')
file.write("Hi Nisam")
file.close()

# append a file

file = open('file.txt', 'a')
file.write("\nare you fine ")
file.close()

# read a file

try:
    with open('file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    print("completed")

# another program
file = open("file1.txt", 'w')
file.write('hi saliha')
file.close()
try:
    file = open('file1.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("the file doesn`t exist")
    file.close()
finally:
    print("done")
