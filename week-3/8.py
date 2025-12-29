def is_divisible_by_digits(n):
    if n == 0:
        return False
    for d in str(n):
        if int(d) == 0 or n % int(d) != 0:
            return False
    return True

n = int(input("n: "))
nums = [i for i in range(1, n+1) if is_divisible_by_digits(i)]
print(' '.join(map(str, nums)))

print("\nswap array")
m = int(input("length: "))
a = list(map(int, input("numbers: ").split()))

print("before:", ' '.join(map(str, a)))

if len(a) >= 2:
    a[0], a[-1] = a[-1], a[0]

print("after:", ' '.join(map(str, a)))