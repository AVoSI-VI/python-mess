
import sys

def split_by_upperCase(word: str):
    split_word = ""
    for i in range(1, len(word)):
        if word[i].isupper():
            upper_case = word[i]
            split_word = raw_str.replace(upper_case, f" {upper_case}", 1)
    return split_word.lower().replace("()", "")
    
def combine_by_space(word: str):
    split_word = word.split()
    combined_word = split_word[0]
    for wd in split_word[1:]:
        combined_word += wd.capitalize()
    return combined_word
    

userInput = sys.stdin.readlines()
outputs = []
for line in userInput:
    tokens = line.strip().split(";")
    raw_str:str = tokens[2]
    
    formatted_str = ""
    if tokens[0] == "S":
        formatted_str = split_by_upperCase(raw_str)
    else:
        combined_word = combine_by_space(raw_str)
        if tokens[1] == "V":
            formatted_str = combined_word
        elif tokens[1] == "M":
            formatted_str = f"{combined_word}()"
        else:
            first_letter = combined_word[0]
            formatted_str = combined_word.replace(first_letter, first_letter.upper(), 1)
            
    outputs.append(formatted_str)
    
for output in outputs:
    print(output)