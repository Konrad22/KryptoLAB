import sys
import random

#opens file <filename>, reads text of the file into a variable, closes file, returns variable
def read(filename):
    f = open(filename, "r")
    t = f.read()
    f.close()
    return t

#opens file <filename>, writes text <text> into the file, closes file
def write(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

def Diffie_Hellman_key_exchange(bitlength):

    prim = 
    print('Primzahl: ' + prim)
    generator = calc_generator(prim)
    print('Generator: ' + generator)
    a = random.randint(0, prim)
    b = random.randint(0, prim)
    A = (generator**a) % prim
    calc_Alice = 'A = ' + generator + '^' + a + ' mod ' + prim + '\n' + 'A = ' + A
    print(calc_Alice)
    B = (generator**b) % prim
    calc_Bob = 'B = ' + generator + '^' + b + ' mod ' + prim + '\n' + 'B = ' + B
    print(calc_Bob)
    if (A**b)%prim == (B**a)%prim:
        shared_key = A**b%prim
    else:
        print('Fehler ist passiert')
        return
    print('Gemeinsamer Schlüssel: ' + shared_key)
    return

#calculates a generator for a prim number <prim>
def calc_generator(prim, prim_factors):
    while():
        a = random.randint(1, prim-1)
        for i in range(len(prim_factors)):
            exponent = prim * prim_factors[i]
            if a**exponent == 1:
                break
        return a