row = 5
for i in range(1, 6):
    for space in range(row - i):
        print(" ", end=" ")
    for star in range(i):
        print(" * ", end=" ")
    print()
