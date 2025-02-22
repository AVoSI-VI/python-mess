def all_the_longest(l1: list):
    b = l1[0]
    l2 = []
    for blah in l1:
        if len(blah) > len(b):
            b = blah
    for nah in l1:
        if len(nah) == len(b):
            l2.append(nah)
        
    return l2


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']