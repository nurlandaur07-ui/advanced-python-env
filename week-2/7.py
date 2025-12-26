from collections import Counter

items = input().split()
freq = Counter(items)

print("Purchase frequency:")
for item, count in freq.items():
    print(item + ":", count)

popular = freq.most_common(1)[0][0]
print("\nMost popular item:", popular)

once = [item for item, count in freq.items() if count == 1]
print("\nPurchased once:", " ".join(once))

print("\nSorted by frequency:")
for item, count in freq.most_common():
    print(item, count)