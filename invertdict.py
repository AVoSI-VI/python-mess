def invert(dictionary: dict):
    s2 = {}
    for key, value in dictionary.items():
        s2[key] = value
    s.clear()
    for k, v in s2.items():
        s[v] = k



s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)