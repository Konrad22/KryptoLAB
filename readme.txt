tasks not done:
U06, U07, U11



Additive Cypher
encrypt.py
python encrypt.py [inputfile] [key] [outputfile]

decrypt.py
python decrypt.py [inputfile] [key] [outputfile]

automatic_decrypt.py
python automatic_decrypt.py [input.txt]


Viginere
encrypt.py
python encrypt.py [inputfile] [key] [outputfile]

decrypt.py
python decrypt.py [inputfile] [key] [outputfile]

automatic_decrypt.py
python automatic_decrypt.py [inputfile] [outputfile]


Betriebsmodi
No programms.


AES
encrypt_AES.py
python encrypt_AES.py [Betriebsmodus] [inputfile] [keyfile] [outputfile] ([initializing vector] if needed)
Betriebsmodi: ECB, CBC, OFB, CTR
keyfile contains all 11 roundkeys

decrypt_AES.py
python decrypt_AES.py [Betriebsmodus] [inputfile] [keyfile] [outputfile] ([initializing vector] if needed)
Betriebsmodi: ECB, CBC, OFB, CTR
keyfile contains all 11 roundkeys


AESKeyGen
encrypt_modi_AES.py
python encrypt_modi_AES.py [Betriebsmodus] [inputfile] [keyfile] [outputfile] ([initializing vector] if needed)
keyfile contains only first roundkey

decrypt_modi_AES.py
python decrypt_modi_AES.py [Betriebsmodus] [inputfile] [keyfile] [outputfile] ([initializing vector] if needed)
keyfile contains only first roundkey


RSA
encrypt_RSA.py
python encrypt_RSA.py [inputfile] [key] [outputfile]
inputfile contains single decimal number
key is a pair (a, n), either the public or the private key


RSAKey
RSAKeyGen.py
python RSAKeyGen.py [length] [outputfile_private] [outputfile_public] [used primes]
length refers to the approximate desired length of the binary representation of the primes used
the outputfiles will contain the private and public key each


Diffie-Hellman
diffie_hellman_key_calc.py
python diffie_hellman_key_calc.py [length]
length refers to the approximate desired length of the binary representation of the prime used
