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
    return cypher_text

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
    return plain_text
    
    
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
    for h in range(len(hex_list)):
        int_list[h] = hex_to_int(hex_list[h])
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
def prepare_text(textfile):
    text_list = transform_byteblock_into_bytelist(textfile)
    text_list = hex_list_to_int(text_list)
    return text_list

#transforms SBox bytes and SBoxInvers bytes into lists of integer
def prepare_SBox_and_SBoxInvers(SBoxfile, SBoxInversfile):
    SBox_list = transform_byteblock_into_bytelist(SBoxfile)
    SBox_list = hex_list_to_int(SBox_list)
    SBoXInvers_list = transform_byteblock_into_bytelist(SBoxInversfile)
    SBoXInvers_list = hex_list_to_int(SBoXInvers_list)
    return SBox_list, SBoXInvers_list

#XORs two list of integers elementwise
def XOR_list(list1, list2):
    c = len(list1)
    list3 = [0]*c
    for i in range(c):
        list3[i] = list1[i] ^ list2[i]
    return list3

#Adds RoundKey to <byte_list>
def AddRoundKey(byte_list, key_list):
    byte_list_key = XOR_list(byte_list, key_list)
    return byte_list_key

#substitutes the integers in <byte_list> with integers of the SBox
def SubBytes(byte_list):
    byte_list_mod = [None]*len(byte_list)
    SBox_list = transform_byteblock_into_bytelist('SBox.txt')
    SBox_list = hex_list_to_int(SBox_list)
    for i in range(len(byte_list)):
        byte_list_mod[i] = SBox_list[byte_list[i]]
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

#calculates x**(i−1) in GF(2**8) by looking it up in a table and returns that number multiplied by 2**24
def rcon(i):
    table = read('rc(i)_table.txt').split()
    rc_i = table[i-1]
    return hex_to_int(rc_i + '000000')

#takes a word <word> and does two cyclical leftshift, returns an 8bit string
def rotWord(word):
    hex_word = int_to_hex(word).zfill(8)
    rotWord = hex_word[2:] + hex_word[:2]
    return rotWord

#applies SubBytes to the 4 bytes in the word <word>, returns an int <subWord_int>
def SubWord(word):
    byte_list = [None]*4
    for i in range(4):
        byte_list[i] = word[2*i:2*i+2]
    byte_list_int = hex_list_to_int(byte_list)
    subBytes = SubBytes(byte_list_int)
    subBytes_hex = int_list_to_hex(subBytes)
    subWord = subBytes_hex[0]
    for i in range(1,4):
        subWord = subWord + subBytes_hex[i]
    subWord_int = hex_to_int(subWord)
    return subWord_int

#takes the list <key_words> which consists of four words (meaning 32 bits) and generates the list <round_keys> with 44 words based on the words in <key_words>
def key_Gen(key_words):
    key_words_int = hex_list_to_int(key_words)
    round_keys = [None]*44
    for i in range(len(round_keys)):
        if i < 4:
            round_keys[i] = key_words_int[i]
        elif i % 4 == 0:
            round_keys[i] = round_keys[i-4] ^ rcon(i//4) ^ SubWord(rotWord(round_keys[i-1]))
        else:
            round_keys[i] = round_keys[i-4] ^ round_keys[i-1]
    for i in range(len(round_keys)):
        round_keys[i] = int_to_hex(round_keys[i]).zfill(8)
    return round_keys

#assumes the first roundkey is being handed as a file containing 16 bytes and splits them in 4 words
#generates the rest of the roundkeys from the first roundkey and returns the whole list of roundkeys
def prepare_key(keyfile):
    list_of_intial_keys = transform_byteblock_into_bytelist(keyfile)
    list_of_key_words = [None] * 4
    for i in range(4):
        list_of_key_words[i] = list_of_intial_keys[i*4]
        for j in range(1, 4):
            list_of_key_words[i] = list_of_key_words[i] + list_of_intial_keys[i*4 + j]
    round_keys = key_Gen(list_of_key_words)
    round_keys_list = [None]*11
    for i in range(11):
        round_words = round_keys[i*4:(i+1)*4]
        round_keys_list[i] = [None]*16
        for j in range(16):
            round_keys_list[i][j] = round_words[j//4][(2*j)%8:(2*j)%8+2]
    round_keys_list_int = [None]*11
    for i in range(11):
        round_keys_list_int[i] = hex_list_to_int(round_keys_list[i])
    return round_keys_list_int