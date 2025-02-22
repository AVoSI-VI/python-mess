from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    a = leg1 ** 2
    b = leg2 ** 2
    c = a + b
    return sqrt(c)

print(hypotenuse(3,4)) # 5.0
print(hypotenuse(5,12)) # 13.0
print(hypotenuse(1,1)) # 1.4142135623730951