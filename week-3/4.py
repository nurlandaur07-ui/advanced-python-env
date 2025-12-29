def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divide_fractions(a, b, c, d):
    numerator = a * d
    denominator = b * c
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def is_inside_circle(x, y, xc, yc, r):
    return (x - xc)**2 + (y - yc)**2 <= r**2

print("fraction division")
a = int(input("numerator 1 (a): "))
b = int(input("denominator 1 (b): "))
c = int(input("numerator 2 (c): "))
d = int(input("denominator 2 (d): "))
if b == 0:
    raise ValueError("denominator 1 (b) must not be zero")
if d == 0:
    raise ValueError("denominator 2 (d) must not be zero")
if c == 0:
    raise ValueError("cannot divide by a zero fraction (numerator 2 (c) is 0)")
num, den = divide_fractions(a, b, c, d)
print("result:", num, "/", den)

print("\npoints inside circle")
xc = float(input("center x: "))
yc = float(input("center y: "))
r = float(input("radius: "))
points = []
for name in ['p', 'f', 'l']:
    x = float(input(f"{name} x: "))
    y = float(input(f"{name} y: "))
    points.append((name, x, y))

count = 0
for name, x, y in points:
    if is_inside_circle(x, y, xc, yc, r):
        print(f"point {name} is inside")
        count += 1
    else:
        print(f"point {name} is outside")
print("total points inside:", count)