row = 6
for i in range(1, 6):
    for space in range(i, row - 1):
        print("   ", end="")
    for star in range(i):
        print(" * ", end="")
    print()
