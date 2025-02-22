i = int(input("Please type in a number: "))
index1 = 0
index2 = -1
i1 = 1
ar = ""
while index1 < i / 2:
    while i1 <= i:
        ar += str(i1)
        i1 += 1
        #print(ar)
    print(ar[index1])
    if ar[index1] != ar[index2]:
        print(ar[index2])
    index1 += 1
    index2 -= 1
    