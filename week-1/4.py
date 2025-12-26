n = int(input())
s = 0
if n >= 1:
    for i in range(1, n + 1):
        s += i
else:
    for i in range(n, 2):
        s += i
print(s)