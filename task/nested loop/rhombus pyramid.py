num = 5
for i in range(5):
    for space in range(num + i):
        print(" ", end="")
    for star in range(4):
        print("   *", end="")
    print()
