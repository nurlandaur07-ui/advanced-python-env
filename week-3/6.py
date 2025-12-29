def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("gcd and lcm")
a = int(input("first number: "))
b = int(input("second number: "))
print("gcd: ", gcd(a, b))
print("lcm: ", lcm(a, b))

print("\narea of convex quadrilateral")
a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))
d = float(input("side d: "))
p = float(input("diagonal p: "))

s1 = (a + b + p) / 2
area1 = (s1 * (s1 - a) * (s1 - b) * (s1 - p)) ** 0.5

s2 = (c + d + p) / 2
area2 = (s2 * (s2 - c) * (s2 - d) * (s2 - p)) ** 0.5

print("area: ", area1 + area2)