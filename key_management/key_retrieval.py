#!/usr/bin/env python
#coding: utf-8
#https://cryptography.io/en/latest/

from secretsharing import PlaintextToHexSecretSharer

ids = []
shares = []
no_of_chars = []

# get the number of lines of our key
with open("lines.txt", 'r') as lines:
    sh = int(lines.readline()) #  required shares
    n = int(lines.readline())  #  number of lines

print("Napíšte " + str(sh) + " ID použité na obnovu kľúča.")
for i in range(sh):
    ids.append(int(input()))

# for each line open shares
for l in range(n):
    new_share = []
    for s in range(sh):
        dir = "shares" + str(ids[s]) + "/"
        fname = "share" + str(ids[s]) + "_" + str(l) + ".txt"
        try:
            with open(dir + fname, 'rb') as f:
                new_share.append(f.read())
        except FileNotFoundError:
            print("Chyba: Súbor sa nenašiel.")
    shares.append(new_share)

#print(shares)

with open("privatekey.asc", 'w') as file:
    for l in range(n):
        secretLine = PlaintextToHexSecretSharer.recover_secret(shares[l][0:sh])
        file.write(secretLine)

print("Kľúč bol úspešne obnovený do súboru privatekey.asc")
