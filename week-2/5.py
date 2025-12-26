letters = set("ABCEHKMOPTXY")
n = int(input())

for i in range(n):
    plate = input().strip()

    meow = (
        len(plate) == 6 and
        plate[0] in letters and
        plate[4] in letters and
        plate[5] in letters and
        plate[1:4].isdigit()
    )

    print("Yes" if meow else "No")