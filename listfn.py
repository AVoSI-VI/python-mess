def range_of_list(l1: list):
    s = sorted(l1)
    r = s[-1] - s[0]
    return r

if __name__ == "__main__":
    l2 = [8, 2, 40, 32, 200]
    result = range_of_list(l2)
    print("mean value is:", result)