import sys

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

#encrypts a 128 bitblock of plaintext using AES cypher
#input is the bitblock and the 11 roundkeys (also 128 bitblocks)    
#returns an encrypted 128 bitblock
#function 'prepare_text_and_key' needs to be called ahead of time
def encrypt_AES_128_bitblock(plaintext, key_list):
    text = AddRoundKey(plaintext, key_list[0])
    for i in range(1, 10):
        text = SubBytes(text)
        text = ShiftRows(text)
        text = MixColumns(text)
        text = AddRoundKey(text, key_list[i])
    text = SubBytes(text)
    text = ShiftRows(text)
    cypher_text = AddRoundKey(text, key_list[10])
    return cypher_text
    
#transform input byteblock into bytelist
def transform_byteblock_into_bytelist(filename):
    t = read(filename)
    byte_list = t.split()
    return byte_list

#transforms byte into integer representation
def hex_to_int(hex_number):
    int_number = int(hex_number,16)
    return int_number

#transform list of bytes into list of integer
def hex_list_to_int(hex_list):
    int_list = []
    for hex in hex_list:
        int_list = hex_to_int(hex)
    return int_list

#transforms text bytes and key bytes into lists of integer
def prepare_text_and_key(text, keys):
    text_list = transform_byteblock_into_bytelist(text)
    text_list = hex_list_to_int(text_list)
    list_of_keys = keys.splitlines()
    for key in list_of_keys:
        key_list = key.split()
        key_list = hex_list_to_int(key)
    return text_list, list_of_keys

#transforms SBox bytes and SBoxInvers bytes into lists of integer
def prepare_SBox_and_SBoxInvers()

#XORs two list of integers elementwise
def AddRoundKey(byte_list, key_list):
    for byte in byte_list:
        byte_list[byte] = byte_list[byte] ^ key_list[byte]
    return byte_list


def SubBytes(byte_list):
