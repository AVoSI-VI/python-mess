def print_squares(sq: list, size: int):
    row = 0
    
    while row < size:
        for blah in range(len(sq[row])):
            if sq[row][blah] == 0:
                print("_ ", end="")
            else:
                print(f'{sq[row][blah]} ', end="")
        print()
        row += 1

def inner_squares(l2: list, lb: int, rb: int, tb: int, bb: int, l: int, l3: list):
    row = 0
    
    while row < bb:
        for i in range(lb, rb):
            if row == tb or row == bb - 1:
                l2[row][i] = letters[layers-l]
            if row not in l3:
                if i == lb or i == rb - 1:
                    l2[row][i] = letters[layers-l]
        row += 1
    return l2

def make_square():
    b = amount[layers - 1]
    left_boundary = 1
    right_boundary = b - 1
    top_boundary = 1
    bottom_boundary = b - 1
    la = 2
    nr = 0
    l3 = [0]

    l1 = [[letters[layers-1]] * b for blah in range(b)]
    while b>0:
        inner_squares(l1, left_boundary, right_boundary, top_boundary, bottom_boundary, la, l3)
        b -= 1
        left_boundary += 1
        right_boundary -= 1
        top_boundary += 1
        bottom_boundary -= 1
        la += 1
        nr += 1
        l3.append(nr)
    
    return l1
 
layers = int(input("Number of layers: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
amount = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]
print_squares(make_square(), amount[layers - 1])