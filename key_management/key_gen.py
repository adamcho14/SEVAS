#!/usr/bin/env python
#coding: utf-8

import gnupg
# from key_management import key_sharing_func as share

gpg = gnupg.GPG()
input_data = gpg.gen_key_input(name_email='voting@voting.com',
                               passphrase='matfyzjein')
key = gpg.gen_key(input_data)

pub_key = gpg.export_keys(key)
priv_key = gpg.export_keys(key, True)

with open("mypublickey.asc", 'w') as pubf:
    pubf.write(pub_key)

#save_to =input("Chcete uložiť do súboru aj súkromný kľúč (y/n)?")

#if save_to == "y":
with open("myprivatekey.asc", 'w') as prif:
    prif.write(priv_key)

# share.sharekey(priv_key)


