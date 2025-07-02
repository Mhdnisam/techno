num = 5
for i in range(5, 0, -1):
    for space in range(num - i):
        print("   ", end=" ")
    for star in range(i):
        print(" * ", end=" ")
    print()
