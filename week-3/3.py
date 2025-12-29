import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("two right triangles")
print("triangle 1")
a1 = float(input("leg a: "))
b1 = float(input("leg b: "))
h1 = hypotenuse(a1, b1)
print(f"hypotenuse: {h1:.2f}")

print("\ntriangle 2")
a2 = float(input("leg a: "))
b2 = float(input("leg b: "))
h2 = hypotenuse(a2, b2)
print(f"hypotenuse: {h2:.2f}")

if h1 > h2:
    print("first triangle has larger hypotenuse")
elif h2 > h1:
    print("second triangle has larger hypotenuse")
else:
    print("hypotenuses are equal")

print("\nword letters sorting\n")
text = input("enter text: ")
words = text.split()
sorted = [' '.join(sorted(word)) for word in words]
print("result:", ' '.join(sorted))