def double_items(numbers: list):
    num2 = []
    for blah in range(len(numbers)):
        num2.append(numbers[blah] * 2)
    return num2

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)