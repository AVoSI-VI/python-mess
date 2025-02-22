def read_input(s: str, x: int, y: int):
    while True:
        try:
            inp = input(s)
            n = int(inp)
            if n > x and n < y or n < x and n > y:
                return n
        except ValueError:
            pass

number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)