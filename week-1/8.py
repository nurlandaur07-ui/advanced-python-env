t = input()
print("YES" if sum(map(int, t[:3])) == sum(map(int, t[3:])) else "NO")
