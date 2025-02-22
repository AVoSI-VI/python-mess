def longest(l1: list):
    l2 = ""
    for blah in l1:
        if len(blah) > len(l2):
            l2 = blah
    return l2


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
