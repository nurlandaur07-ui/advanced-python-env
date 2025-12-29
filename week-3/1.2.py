print("Sum and mean")
for i in range(3):
    nums = list(map(int, input("Enter numbers for array " + str(i+1) + ": ").split()))
    total = sum(nums)
    if len(nums) > 0:
        mean = total / len(nums)
    else:
        mean = 0
    print("Array", i+1, ": Sum =", total, ", Mean =", mean)