import string

def separate_characters(my_string: str):
    l1 = ["", "", ""]
    for slah in my_string:
        if slah in string.ascii_letters:
            l1[0] += slah
        elif slah in string.punctuation:
            l1[1] += slah
        else:
            l1[2] += slah
    return l1

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])