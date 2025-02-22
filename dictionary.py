def times_ten(start_index: int, end_index: int):
    d1 = {}
    for blah in range(start_index, end_index + 1):
        d1[blah] = blah * 10

    return d1

d = times_ten(3, 6)
print(d)