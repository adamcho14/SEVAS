#!/usr/bin/env python
# coding: utf-8

import sqlite3

cont = True
connection = sqlite3.connect("../db/persons.sqlite")

while cont:
    name = input("Meno kandidáta: ")
    surname = input("Priezvisko kandidáta: ")

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM candidates WHERE first_name=? AND last_name=?", (name,surname,))
    result = cursor.fetchall()

    if result == [(0,)]:
        cursor.execute("SELECT COUNT(*) FROM candidates")
        result2 = cursor.fetchall()
        noc = result2[0][0] + 1
        cursor.execute("INSERT INTO candidates VALUES(?,?,?)", (noc,name,surname,))
        print("Kandidát pridaný.")
        connection.commit()
    else:
        print("Kandidát už existuje v db.")

    inp = input("Pridať ďalšieho kandidáta (y/n)?")

    if inp == "n":
        cont = False

connection.close()
