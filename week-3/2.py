import math

def triangle_area(base, height):
    return 0.5 * base * height

def hexagon_area(a):
    return 6 * triangle_area(a, a * math.sin(math.pi / 3))

a = float(input("Side of hexagon: "))
print("Hexagon area:", hexagon_area(a))

print("\n Three rectangles")
for i in range(3):
    print("Rectangle", i+1)
    l = float(input("  Length: "))
    w = float(input("  Width: "))
    print("  Area:", l * w)