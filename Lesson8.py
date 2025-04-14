import time

a = int(input("Please Enter The first Value:"))
time.sleep(2)
b = int(input("Please Enter The Second Value:"))
time.sleep(2)
c = int(input("Please Enter The Third Value:"))

d = a
a = c
c = b
b = d

time.sleep(2)
print("Values after Swapping:", "\n", a, "\n", b, "\n", c)