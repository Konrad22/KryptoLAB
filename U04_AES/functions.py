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
    #for i in range(1, 2):
        text = SubBytes(text)
        text = ShiftRows(text)
        text = MixColumns(text)
        text = AddRoundKey(text, key_list[i])
    text = SubBytes(text)
    text = ShiftRows(text)
    cypher_text = AddRoundKey(text, key_list[10])
    return ' '.join(int_list_to_hex(cypher_text))

#decrypts a 128 bitblock of cyphertext using AES cypher
#input is the bitblock and the 11 roundkeys (also 128 bitblocks)    
#returns an decrypted 128 bitblock
#function 'prepare_text_and_key' needs to be called ahead of time
def decrypt_AES_128_bitblock(cyphertext, key_list):
    text = AddRoundKey(cyphertext, key_list[10])
    text = ShiftRowsInvers(text)
    text = SubBytesInvers(text)
    for i in range(1, 10):
    #for i in range(1, 2):
        text = AddRoundKey(text, key_list[10-i])
        text = MixColumnsInvers(text)
        text = ShiftRowsInvers(text)
        text = SubBytesInvers(text)
    plain_text = AddRoundKey(text, key_list[0])
    return ' '.join(int_list_to_hex(plain_text))
    
    
#transform input byteblock into bytelist
def transform_byteblock_into_bytelist(filename):
    t = read(filename)
    byte_list = t.split()
    return byte_list

#transforms hex into integer representation
def hex_to_int(hex_number):
    int_number = int(hex_number,16)
    return int_number

#transform list of hex number into list of integer
def hex_list_to_int(hex_list):
    int_list = [None]*len(hex_list)
    for hex in range(len(hex_list)):
        int_list[hex] = hex_to_int(hex_list[hex])
    return int_list

#transforms int into hex representation
def int_to_hex(int_number):
    hex_number = hex(int_number).lstrip("0x")
    if int_number < 16:
        hex_number = '0' + hex_number
    return hex_number

#transform list of integer into list of hex numbers
def int_list_to_hex(int_list):
    hex_list = [None]*len(int_list)
    for int in range(len(int_list)):
        hex_list[int] = int_to_hex(int_list[int])
    return hex_list

#transforms text bytes and key bytes into lists of integer
def prepare_text_and_key(textfile, keysfile):
    text_list = transform_byteblock_into_bytelist(textfile)
    text_list = hex_list_to_int(text_list)
    keyfile = read(keysfile)
    list_of_keys = keyfile.splitlines()
    for i in range(len(list_of_keys)):
        list_of_keys[i] = list_of_keys[i].split()
        list_of_keys[i] = hex_list_to_int(list_of_keys[i])
    return text_list, list_of_keys

#transforms SBox bytes and SBoxInvers bytes into lists of integer
def prepare_SBox_and_SBoxInvers(SBoxfile, SBoxInversfile):
    SBox_list = transform_byteblock_into_bytelist(SBoxfile)
    SBox_list = hex_list_to_int(SBox_list)
    SBoXInvers_list = transform_byteblock_into_bytelist(SBoxInversfile)
    SBoXInvers_list = hex_list_to_int(SBoXInvers_list)
    return SBox_list, SBoXInvers_list

#XORs two list of integers elementwise
def AddRoundKey(byte_list, key_list):
    byte_list_key = [None]*len(byte_list)
    for byte in range(len(byte_list)):
        byte_list_key[byte] = byte_list[byte] ^ key_list[byte]
    return byte_list_key

#substitutes the integers in <byte_list> with integers of the SBox
def SubBytes(byte_list):
    byte_list_mod = [None]*len(byte_list)
    SBox_list = transform_byteblock_into_bytelist('SBox.txt')
    SBox_list = hex_list_to_int(SBox_list)
    for integer in range(len(byte_list)):
        byte_list_mod[integer] = SBox_list[byte_list[integer]]
    return byte_list_mod

#substitutes the integers in <byte_list> with integers of the SBoxInvers
def SubBytesInvers(byte_list):
    byte_list_mod = [None]*len(byte_list)
    SBoXInvers_list = transform_byteblock_into_bytelist('SBoxInvers.txt')
    SBoXInvers_list = hex_list_to_int(SBoXInvers_list)
    for integer in range(len(byte_list)):
        byte_list_mod[integer] = SBoXInvers_list[byte_list[integer]]
    return byte_list_mod

#pretends that the list is a 4x4 array and leftshifts all elements of the list depending
#on what row they are in, 0th row by 0, 1st row by 1, 2th row by 2, 3rd row by 3
def ShiftRows(byte_list):
    shifted_byte_list = [None]*len(byte_list)
    for byte in range(len(byte_list)):
        shift = byte % 4
        shifted_byte_list[byte-4*shift] =  byte_list[byte]
    return shifted_byte_list

#pretends that the list is a 4x4 array and rightshifts all elements of the list depending
#on what row they are in, 0th row by 0, 1st row by 1, 2th row by 2, 3rd row by 3
def ShiftRowsInvers(byte_list):
    shifted_byte_list = [None]*len(byte_list)
    for byte in range(len(byte_list)):
        shift = byte % 4
        shifted_byte_list[byte] =  byte_list[byte-4*shift]
    return shifted_byte_list

#mixes columns according to AES encryption standard
def MixColumns(byte_list):
    mixed_byte_list = [None] * len(byte_list) 
    for i in range(4):
        mixed_byte_list[0 + i*4] = russian_multiplication_initialise(2, byte_list[0 + i*4]) ^ russian_multiplication_initialise(3, byte_list[1 + i*4]) ^ byte_list[2 + i*4] ^ byte_list[3 + i*4]
        mixed_byte_list[1 + i*4] = russian_multiplication_initialise(2, byte_list[1 + i*4]) ^ russian_multiplication_initialise(3, byte_list[2 + i*4]) ^ byte_list[3 + i*4] ^ byte_list[0 + i*4]
        mixed_byte_list[2 + i*4] = russian_multiplication_initialise(2, byte_list[2 + i*4]) ^ russian_multiplication_initialise(3, byte_list[3 + i*4]) ^ byte_list[0 + i*4] ^ byte_list[1 + i*4]
        mixed_byte_list[3 + i*4] = russian_multiplication_initialise(2, byte_list[3 + i*4]) ^ russian_multiplication_initialise(3, byte_list[0 + i*4]) ^ byte_list[1 + i*4] ^ byte_list[2 + i*4]
    return mixed_byte_list

#mixes columns according to AES decryption standard
def MixColumnsInvers(byte_list):
    mixed_byte_list = [None] * len(byte_list) 
    for i in range(4):
        mixed_byte_list[0 + i*4] = russian_multiplication_initialise(14, byte_list[0 + i*4]) ^ russian_multiplication_initialise(11, byte_list[1 + i*4]) ^ russian_multiplication_initialise(13, byte_list[2 + i*4]) ^ russian_multiplication_initialise(9, byte_list[3 + i*4])
        mixed_byte_list[1 + i*4] = russian_multiplication_initialise(14, byte_list[1 + i*4]) ^ russian_multiplication_initialise(11, byte_list[2 + i*4]) ^ russian_multiplication_initialise(13, byte_list[3 + i*4]) ^ russian_multiplication_initialise(9, byte_list[0 + i*4])
        mixed_byte_list[2 + i*4] = russian_multiplication_initialise(14, byte_list[2 + i*4]) ^ russian_multiplication_initialise(11, byte_list[3 + i*4]) ^ russian_multiplication_initialise(13, byte_list[0 + i*4]) ^ russian_multiplication_initialise(9, byte_list[1 + i*4])
        mixed_byte_list[3 + i*4] = russian_multiplication_initialise(14, byte_list[3 + i*4]) ^ russian_multiplication_initialise(11, byte_list[0 + i*4]) ^ russian_multiplication_initialise(13, byte_list[1 + i*4]) ^ russian_multiplication_initialise(9, byte_list[2 + i*4])
    return mixed_byte_list

#double a given binary number smaller than 11111111
def double_function(number):
    binary_number = bin(number)[2:].zfill(8)
    t = (number << 1) % 256
    if binary_number[0] == '1':
        t = t ^ 27
    return t

#returns 0 if one of the multiplicants is 0, otherwise calls a recursive funtions and hands the initalised result and the multiplicants
def russian_multiplication_initialise(multiplicant_1, multiplicant_2):
    if multiplicant_2 < multiplicant_1:
        russian_multiplication_initialise(multiplicant_2, multiplicant_1)
    if multiplicant_1 == 0:
        return 0
    result = 0
    return russian_multiplication_calculation(multiplicant_1, multiplicant_2, result)

#recursive function that adds to <result> if <multiplicant_1> is an odd number
#calls itself if <multiplicant_1> is greater than 1, otherwise it returns <result> + <multiplicant_2>
def russian_multiplication_calculation(multiplicant_1, multiplicant_2, result):
    if multiplicant_1 == 1:
        return result ^ multiplicant_2
    if multiplicant_1 % 2 == 1:
        result = result ^ multiplicant_2
    return russian_multiplication_calculation(multiplicant_1//2, double_function(multiplicant_2), result)