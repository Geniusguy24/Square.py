radius = int(input("Please enter the radius of the circle = "))

def circumference(radius):
    circumference = 2 * 3.1415926535897932384 * radius
    return circumference
result = circumference(radius)
print("The circumference of the circle is", result)