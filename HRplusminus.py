def plusMinus(arr):
    # Write your code here
    l = len(arr)
    p = 0
    n = 0
    z = 0
    for blah in range(len(arr)):
        if arr[blah] < 0:
            n += 1
        elif arr[blah] > 0:
            p += 1
        else:
            z += 1
    print(f"{p/l:.6f}")
    print(f"{n/l:.6f}")
    print(f"{z/l:.6f}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)