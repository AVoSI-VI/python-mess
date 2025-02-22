def count_matching_elements(l1: list, e):
    c = 0
    for i in l1:
        for j in i:
            if j == e:
                c += 1

    return c

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))