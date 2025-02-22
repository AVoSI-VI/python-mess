def histogram(s: str):
    h = {}
    for i in s:
        if i not in h:
            h[i] = 0
        h[i] += 1
    for key, value in h.items():
        print(f"{key}  {"*" * value}")

histogram("statistically")
histogram("abba")
histogram("yodeliehooooooo")