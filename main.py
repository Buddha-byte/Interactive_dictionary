#!/usr/bin/env python3


import json
from difflib import get_close_matches


data = json.load(open("data\\data.json"))


def translate(some_word):
    some_word = some_word.lower()
    if some_word in data:
        return data[some_word]
    elif len(get_close_matches(some_word, data.keys())) > 0:
        match_words = get_close_matches(some_word, data.keys())
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % match_words[0])
        yn = yn.lower()
        if yn == 'y':
            return data[match_words[0]]
        elif yn == 'n':
            return "The word doesn't exist!"
        else:
            return "I don't understand you!"
    else:
        return "The word doesn't exist"


word = input("Enter a word: ")

print(translate(word))
