def breakingRecords(scores):
    # Write your code here
    mini = scores[0]
    maxi = scores[0]
    l1 = [0, 0]
    for blah in range(len(scores)):
        if scores[blah] > maxi:
            maxi = scores[blah]
            l1[0] += 1
        elif scores[blah] < mini:
            mini = scores[blah]
            l1[1] += 1
    return l1
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()