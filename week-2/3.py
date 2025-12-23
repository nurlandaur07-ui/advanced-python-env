n, m = map(int, input().split())
s = input().strip()
subs = set()
for i in range(n - m + 1):
    subs.add(s[i:i+m])
print(len(subs))