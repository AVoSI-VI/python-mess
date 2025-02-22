from fractions import Fraction

def fractionate(amount: int):
    l1 = []
    for blah in range(amount):
        l1.append(Fraction(1, amount))
    return l1
    

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))

print(Fraction(1, 3))