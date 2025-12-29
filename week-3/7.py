def triangle_area(a, b):
    return 0.5 * a * b

def rectangle_area(a, b):
    return a * b

print("quadrilateral with right angle between x and y")
x = float(input("side x: "))
y = float(input("side y: "))
z = float(input("side z: "))
t = float(input("side t: "))

area1 = triangle_area(x, y)
area2 = rectangle_area(z, t)
total = area1 + area2

print("area: ", total)

print("\n10-digit octal with leading zeros")
n = int(input("non-negative integer: "))
octal = f"{n:010o}"
print("octal:", octal)