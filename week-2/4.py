valid_letters = set("ABCEHKMOPTXY")
n = int(input())
for _ in range(n):
    plate = input().strip()
    ok = (
        len(plate) == 6 and
        plate[0] in valid_letters and
        plate[4] in valid_letters and
        plate[5] in valid_letters and
        plate[1:4].isdigit()
    )
    print("Yes" if ok else "No")