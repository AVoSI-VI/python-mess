def formatted(l1: list):
    l2 = []
    for blah in l1:
        f = f"{blah:.2f}"
        l2.append(f)

    return l2



if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)