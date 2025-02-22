import math

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):

        for j in range(i + 1, n):
            #if ar[i] < ar[j]:
                if (ar[i] + ar[j]) % k == 0:
                    count += 1

    return count

        



n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
#print(ar[0] < ar[1] or ar[0] > ar[1] and (ar[0] + ar[1]) % k == 0)
print(divisibleSumPairs(n,k,ar))