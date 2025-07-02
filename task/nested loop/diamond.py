num = 4
for i in range(4):
    for j in range(num + i):
        print("  ", end=" ")
    for star in range(i + 1):
        print(" *", end=" ")
    print()
