def first_word(sentence):
    first = sentence.split()
    return first[0]
def second_word(sentence):
    second = sentence.split()
    return second[1]
def last_word(sentence):
    third = sentence.split()
    return third[-1]

if __name__ == "__main__":
    sentence = "it was"

    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
