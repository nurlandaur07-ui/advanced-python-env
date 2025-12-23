items = input().split()
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
print("Purchase frequency:")
for k, v in freq.items():
    print(f"{k}: {v}")
max_item = max(freq, key=freq.get)
print("\nMost popular item:", max_item)
once = [k for k, v in freq.items() if v == 1]
print("\nPurchased once:", " ".join(once))
print("\nSorted by frequency:")
for k, v in sorted(freq.items(), key=lambda x: -x[1]):
    print(k, v)