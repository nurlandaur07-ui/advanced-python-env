import math

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius * radius

print("Area Calculator")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Choose: "))

if choice == 1:
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = triangle_area(b, h)
    print("Area:", area)
elif choice == 2:
    l = float(input("Length: "))
    w = float(input("Width: "))
    area = rectangle_area(l, w)
    print("Area:", area)
elif choice == 3:
    r = float(input("Radius: "))
    area = circle_area(r)
    print("Area:", area)