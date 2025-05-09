import time

try:

    age = int(input("Please Enter your age: "))
    if age%2 == 0:
        print("Your age is even, but your life is odd!")
    else:
        print("You are odd")

except ValueError as ex:
    print("Exception:", ex)

