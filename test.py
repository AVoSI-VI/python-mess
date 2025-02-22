def spruce(size):
    print("a spruce!")
    n = size
    row = "*"
    n2 = size
    stump = "*"
    while n > 0:
        print(" " * n + row)
        row += "**"
        n -= 1
    print(" " * n2 + stump)


if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)
    spruce(40)