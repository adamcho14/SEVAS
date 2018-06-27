#!/usr/bin/env python

import rsa
# this creates the private and public keys used to encrypt voter's login
(pubkey, privkey) = rsa.newkeys(512)

with open('private.pem', 'wb') as private:
    private.write(privkey.save_pkcs1())

with open('public.pem', 'wb') as public:
    public.write(pubkey.save_pkcs1())
