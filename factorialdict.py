def factorials(n: int):
    d1 = {}
  
    na = 1
    l1 = []
    for blah in range(1, n + 1):
        na = na * blah
        l1.append(na)
    print(l1)
    for i in range(len(l1)):
        d1[i+1] = l1[i]
    return d1

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])