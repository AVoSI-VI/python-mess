def miniMaxSum(arr):
    # Write your code here
    s = sorted(arr)
    mini = 0
    maxi = 0
    for blah in range(len(s) - 1):
        mini += s[blah]
    for slop in range(1, len(arr)):
        maxi += s[slop]
    print(f"{mini} {maxi}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)