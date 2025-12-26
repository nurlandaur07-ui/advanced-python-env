def all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    new_list = []
    for s in lst:
        while len(s) < max_len:
            s += "_"
        new_list.append(s)
    return new_list
print(all_eq(["cat", "dog", "elephant", "fox"]))