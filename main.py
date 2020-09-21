#!/usr/bin/env python3


import json
from difflib import get_close_matches
import time
import mysql.connector




def translate(some_word):
    some_word = some_word.lower()

    con = mysql.connector.connect(
    user = "ardit700_student",
    password="ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

    cursor = con.cursor()

    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % some_word)
    data = cursor.fetchall()

    if data:
        for word in data:
            print(word)
    else:
        return "The word doesn't exist"


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
        time.sleep(3)
else:
    print(output)
