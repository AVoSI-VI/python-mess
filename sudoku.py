def row_correct(sudoku: list, row_no: int):
    #numbers_checked = []
    row = sudoku[row_no]
    numbers_checked = []
    for column in row:
        if column in numbers_checked:
            return False
        if column != 0:
            numbers_checked.append(column)
    return True

def column_correct(sudoku: list, column_no: int):
    numbers_checked = []
    for row in sudoku:
        if row[column_no] in numbers_checked:
            return False
        if row[column_no] != 0:
            numbers_checked.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    check_row = row_no
    numbers_checked = []
    while check_row < (row_no + 3):
        
        row = sudoku[check_row]
        for i in range(column_no, column_no + 3):     
            if row[i] in numbers_checked:
                return False
            if row[i] != 0:
                numbers_checked.append(row[i])
        check_row += 1
    return True
def sudoku_grid_correct(sudoku: list):
    blocks = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
    rows = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    columns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    yar = False
    check = 0
    l1 = []
    while check < 9:
       # if row_correct(sudoku, check) and column_correct(sudoku, check) and block_correct(sudoku, blocks[check][0], blocks[check][1]) is True:
       #     yar = True
       # else:
       #     yar = False
        #print(row_correct(sudoku, check))
        #print(column_correct(sudoku, check))
        #print(block_correct(sudoku, blocks[check][0], blocks[check][1]))
        l1.append(row_correct(sudoku, check))
        l1.append(column_correct(sudoku, check))
        l1.append(block_correct(sudoku, blocks[check][0], blocks[check][1]))
        check += 1
        
    for blah in l1:
        if l1[blah] == False:
            return False
    return True
    
def print_sudoku(sudoku: list):
    row = 0
    
    while row < 9:
        for blah in range(len(sudoku[row])):
            if sudoku[row][blah] == 0:
                print("_ ", end="")
            else:
                print(f'{sudoku[row][blah]} ', end="")
        print()
        row += 1

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    s_copy = [row[:] for row in sudoku]
    s_copy[row_no][column_no] = number
    return s_copy


sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)