#/usr/bin/env python3


import json
from difflib import get_close_matches


data = json.load(open("data\\data.json"))


def translate(some_word):
    some_word = some_word.lower()
    some_word = get_close_matches(some_word, data.keys())[0]
    if some_word in data:
        return data[some_word]
    else:
        return("The word doesn't exist")


word = input("Enter a word: ")

print(translate(word))
