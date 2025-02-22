l1 = []

while True:
    number = int(input("New item "))
    if number != 0:
        l1.append(number)
    else:
        print("Bye!")
        break
    print(f"The list now: {l1}")
    l2 = sorted(l1)
    print(f"The list in order: {l2}")