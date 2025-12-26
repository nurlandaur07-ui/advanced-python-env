eq = input().strip()
a, op, b, _, c = eq
def val(x):
    return int(x)
if a == 'x':
    b, c = val(b), val(c)
    print(c - b if op == '+' else b - c)
elif b == 'x':
    a, c = val(a), val(c)
    print(c - a if op == '+' else a - c)
else:
    a, b = val(a), val(b)
    print(a + b if op == '+' else a - b)