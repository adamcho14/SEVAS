#!/usr/bin/env python
# coding: utf-8

import json
import sys
import config as can_n

CAND_NUM = can_n.CAND_NUM


# this function selects candidates from the database
def select_candidates():
    try:
        with open('candidates.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        sys.exit("Požadovaný súbor candidates.txt sa nenašiel")


def decrypt(s):
    #mime = SMIME.SMIME()

    #mime.load_key('priv.pem', 'cert.pem')
    #with open("tmp.p7", 'w') as f:
        #f.write(s)
    #p7, data = SMIME.smime_load_pkcs7("tmp.p7")
    #try:
        #return mime.decrypt(p7)
    #except SMIME.PKCS7_Error as err:
        #print("Chyba pri dešifrovaní: " + str(err))
        #return "0"
        return s


# this function creates a list out of given string
def parse(s):
    return list(s)


# this function validates given list. It only checks if it is in the vote form
# state values:
# 0 ... we expect '<',
# 1 ... we expect the first digit of key,
# 2 ... we expect '#' or a digit,
# 3 ... we expect the first digit of value,
# 4 ... we expect '>' or a digit
def validate(l):
    state = 0
    for i in l:
        if state == 0:  # checking '<'
            if i != '<':
                return False
            state = 1  # continue by checking key
        elif state == 1:  # we need to have at least one digit after '<'
            if not i.isdigit():
                return False
            state = 2
        elif state == 2:  # now we can have either a digit or '#'
            if i != '#' and not i.isdigit():
                return False
            if i == '#':
                state = 3
        elif state == 3:  # after '#' we expect a digit
            if not i.isdigit():
                return False
            state = 4
        elif state == 4:  # now we can have either a digit or '>'
            if i != '>' and not i.isdigit():
                return False
            if i == '>':
                state = 0
    if state == 0:  # the vote has to end with '>'
        return True
    else:
        return False


# this function gets values in given list. List must be validated beforehand.
# it also checks whether there is no more yeses than allowed. If there is, it changes the vote to 0.
def get_values(l):
    if not validate(l):
        return 0

    cand = []
    for c in candidates:
        cand.append(c[0])
    num = 0  # checks the number of yeses
    values = {}
    j = 1  # the first number in the string
    while j < len(l):
        key = 0
        val = 0
        while l[j] != '#':
            key = 10*key + int(l[j])
            j += 1
        j += 1  # the first number after "#"
        while l[j] != '>':
            val = 10*val + int(l[j])
            j += 1
        if val == 1:
            num += 1
        if (key in values) or (key not in cand) or (val not in election_values):
            print("Neplatný hlas: " + str(l))
            return 0
        values[key] = val
        j += 2  # the first number after "<" ... need to jump "><"

    if num > CAND_NUM:
        return 0

    return values

try:
    with open('votes.txt', 'r') as file:
        votes = json.load(file)  # creates a list of votes out of the json file
except FileNotFoundError:
    sys.exit("Požadovaný súbor votes.txt sa nenašiel")

election_yes = {}
election_no = {}
election_dk = {}
candidates = select_candidates()
election_values = [1, 2, 3]
vote_values = []  # list of dictionaries containing votes

for i in votes:
    if i[0] != "0":
        new_vote = get_values(parse(decrypt(i[0])))
        if new_vote != 0:
            vote_values.append(new_vote)

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
