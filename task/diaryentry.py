# Personal Diary Logger
# 	Create a DiaryEntry class. Let users write and save daily logs into a text file named by date. Allow reading previous entries.

filename = "a.txt"
print("enter your dairy")
print("1.write dairy")
print("2.read diary")
choice = input("enter your choice")
if choice == 1:
    entry = input("write your thoughts")
    with open(filename, "w") as file:
        file.write("entry")
        print("saved")
if choice == 2:
    with open(filename, "r") as file:
        file.read(filename)
    print("file opened")
else:
    print("file note found")
