c = input("Please Enter A charachter:")

if len(c)>1:
    print("Invalid Input! Don't tease me")
else:
    if c >= 'a' and c <= 'z':
        print("It's an elphabet")
    elif c >= 'A' and c <= 'Z':
        print("It's an elphabet")
    else:
        print("It's not an elphabet!")
