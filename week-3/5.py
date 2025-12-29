def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(a, b, c, d):
    numerator = a * d - b * c
    denominator = b * d
    if numerator == 0:
        return 0, 1
    common = gcd(abs(numerator), denominator)
    return numerator // common, denominator // common

print("fraction subtraction")
a = int(input("numerator 1 (a): "))
b = int(input("denominator 1 (b): "))
c = int(input("numerator 2 (c): "))
d = int(input("denominator 2 (d): "))
num, den = subtract_fractions(a, b, c, d)
print("result: ", num, "/", den)

print("\ndivisors of number")
n = int(input("number: "))
divisors = [i for i in range(1, n+1) if n % i == 0]
print("divisors:", ' '.join(map(str, divisors)))