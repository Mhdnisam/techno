try:
    a = int(input("enter a number"))
    b = int(input("enter next number"))
    print("answer = ", a / b)
except ValueError:
    print("values are error")
except ZeroDivisionError:
    print("division not possible.")
finally:
    print("completed")
