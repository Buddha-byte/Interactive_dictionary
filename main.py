#!/usr/bin/env python3


import json
from difflib import get_close_matches
import time
import mysql.connector




def translate(some_word):
    some_word = some_word.lower()

    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    cursor = con.cursor()

    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % some_word)
    data = cursor.fetchall()

    for words_tuple in data:
        if some_word == words_tuple[0]:
            return data
        else:
            if len(get_close_matches(some_word, words_tuple[0])) > 0:
                yn = input("Did you mean: %s? print Y for yes, or N for no" % get_close_matches(some_word, data[0]))
                yn.lower()
                if yn == "y":
                    for word in data:
                        print(word[1])
                        time.sleep(5)
                elif yn == "n":
                    return "The word doesn't exist"
                else:
                    return "I don't understand you!"


word = input("Enter a word: ")

output = translate(word)
