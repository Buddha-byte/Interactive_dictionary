#!/usr/bin/env python3


from difflib import get_close_matches
import time
import mysql.connector


def translate(some_word):
    """
    Return defenition, type: str
    """
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

    if some_word in keys:   # Iteration through the list of expressions from database
        query_01 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % some_word)
        data_query = cursor.fetchall()
        for result in data_query:
            return result[1]
            time.sleep(5)
    elif len(get_close_matches(some_word, keys)) > 0:  # Make a match list from user request
        query_01 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % get_close_matches(some_word, keys)[0])
        data_query = cursor.fetchall()
        for result in data_query:
            return result[1]
            time.sleep(5)
    else:
        return "The word doesn't exist"


word = input("Enter a word: ")

output = translate(word)
