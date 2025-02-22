def create_tuple(x: int, y: int, z: int):
    t1 = (x, y, z)
    t2 = sorted(t1)
    t3 = (t2[0], t2[2], (x+y+z))
    return t3


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
