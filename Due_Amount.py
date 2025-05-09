import time

ba = int(input("Please Enter the total bill amount: "))
time.sleep(1)
ap = int(input("Please Enter the amount you paid: "))
time.sleep(1)

def change(ba, ap):
    if ap >= ba:
        n = ap - ba
        print(f"The Shopkeeper needs to pay you {n} amount of change!")
    else:
        n = ba - ap
        print(f"You need to pay the shopkeeper: {n} amount more!")

change(ba, ap)