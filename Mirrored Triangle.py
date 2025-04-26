rows = int(input("Enter the number of rows for the mirrored triangle: "))


for i in range(rows, 0, -1):
      
    print(' ' * (rows - i) + '*' * i)


