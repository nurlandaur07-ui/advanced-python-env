a = input().strip()
b = input().strip()
n, m = len(a), len(b)

shifts = set()
bb = b + b
for i in range(m):
    shifts.add(bb[i:i+m])

ans = 0
for i in range(n - m + 1):
    if a[i:i+m] in shifts:
        ans += 1
print(ans)