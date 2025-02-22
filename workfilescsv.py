def read_fruits():
    with open("fruits.csv") as file:
        dit = {}
        for line in file:
            line = line.replace("\n", "")
            d_part = line.split(';')
            dit[d_part[0]] = d_part[1]

        return dit
    
print(read_fruits())