eq = input().strip()
a, op, b, _, c = eq

if a == 'x':
    b = int(b)
    c = int(c)
    if op == '+':
        print(c - b)
    else:
        print(b - c)

elif b == 'x':
    a = int(a)
    c = int(c)
    if op == '+':
        print(c - a)
    else:
        print(a - c)

else:
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    else:
        print(a - b)