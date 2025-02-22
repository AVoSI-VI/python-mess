def largest():
    
    with open("numbers.txt") as file:
        lar = 0
        for line in file:
            #line = line.replace("\n", "")
            num = int(line)
            if num > lar:
                lar = num
            print(lar)
        return lar
    
print(largest())