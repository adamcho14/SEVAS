#!/usr/bin/env python
# coding: utf-8

import json
import sqlite3


# this function selects candidates from the database
def select_candidates():
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/candidates.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM candidates")
    result = cursor.fetchall()

    connection.close()

    return result


def decrypt(s):
    return s


# this function creates a list out of given string
def parse(s):
    return list(s)


# this function validates given list
def validate(l):
 return True


# this function gets values in given list. List must be validated beforehand
def get_values(l):
    values = {}
    j = 1 # the first number in the string
    while j < len(l):
        key = 0
        val = 0
        while l[j] != '#':
            key = 10*key + int(l[j])
            j += 1
        j += 1 # the first number afer "#"
        while l[j] != '>':
            val = 10*val + int(l[j])
            j += 1
        values[key] = val
        j += 2 # the first number after "<" ... need to jump "><"
    return values

with open('votes.txt', 'r') as file:
    votes = json.load(file) # creates a list of votes out of the json file

election_yes = {}
election_no = {}
election_dk = {}
candidates = select_candidates()
vote_values = [] # list of dictionaries containing votes

for i in votes:
    vote_values.append(get_values(parse(decrypt(i[0]))))

for c in candidates:
    election_yes[c[0]] = 0
    election_no[c[0]] = 0
    election_dk[c[0]] = 0
    for v in vote_values:
        if v[c[0]] == 1:
            election_yes[c[0]] += 1
        elif v[c[0]] == 2:
            election_no[c[0]] += 1
        elif v[c[0]] == 3:
            election_dk[c[0]] += 1

# print the final results
print("Toto sú výsledky volieb:")
for c in candidates:
    print()
    print(c[1], c[2])
    print("Áno:", election_yes[c[0]])
    print("Nie:", election_no[c[0]])
    print("Zdržali sa:", election_dk[c[0]])
