#!/usr/bin/env python3


from difflib import get_close_matches
import time
import mysql.connector


def translate(some_word):

    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    cursor = con.cursor()

    some_word = some_word.lower()

    query = cursor.execute("SELECT Expression from Dictionary")

    keys = [b[0] for b in cursor.fetchall()]

    matches_words = get_close_matches(some_word, keys)
    if len(matches_words) > 0:
        yn = input("Did you mean %s ? Y for yes or N for no: " % matches_words[0])
        yn.lower()
        if yn == 'y':
            query_01 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % matches_words[0])
            data_query = cursor.fetchall()
            for word_def in data_query:
                print(word_def[1])
                time.sleep(5)
        if yn == 'n':
            print("Try one more time!")
        else:
            print("The word doesn't exist")


word = input("Enter a word: ")

output = translate(word)
