#!/usr/bin/env python
#coding: utf-8
#https://cryptography.io/en/latest/

from secretsharing import PlaintextToHexSecretSharer
import os

n = -1
p = 0
while p > n:
    n = int(input("Number of members of the commission: "))
    p = int(input("Number of people needed to recover the secret: "))
    if p > n:
        print("Invalid input!")

with open("myprivatekey.asc", 'r') as f:
    key = f.readlines()

# every member of the commission is given a part of secret for every line of the key.
# lines have to be reconstructed separately and put together to form the final key
shares = []
i = 0
no_of_chars = []
for l in key:
    no_of_chars.append(len(l))
    shares.append(PlaintextToHexSecretSharer.split_secret(l, p, n))
    #print(shares[i])
    for j in range(n):
        name = "share" + str(j) + "_" + str(i) + ".txt"
        dir = "shares" + str(j) + "/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir + name, 'w') as f:
            f.write(shares[i][j])
    i += 1

with open("lines.txt", 'w') as lines:
    lines.write(str(p) + "\n")
    lines.write(str(i) + "\n")

print("Files share_i_j.txt are produced, "
      "where i is an ID "
      "and j is the number of line of the key they are used for."
      "Shares are stored in directories according to their IDs."
      "Give exactly one directory to every member of the commission.")
