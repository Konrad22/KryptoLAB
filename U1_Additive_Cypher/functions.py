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

#encrypts a text <text> with a key <key> using the additive cypher
def encrypt_additive_cypher_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_cypher_letter_k(l,key)
    return e_text

#decrypts a text <text> with a key <key> using the additive cypher
def decrypt_additive_cypher_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_cypher_letter_k(l,-key)
    return e_text
 
#encrypts a letter <letter> with a key <key> using the additive cypher
def additive_cypher_letter_k(letter, key):
    if(ord(letter)> 64 and ord(letter) < 91):
        letter = transform_number_to_letter((transform_letter_to_number(letter) + key)%26)
    return letter

#transforms the letters of the used alphabet (A-Z) into the numbers 0-25
def transform_letter_to_number(letter):
    n = ord(letter)
    return n-65

#transforms the numbers 0-25 into the letters of the used alphabet (A-Z)
def transform_number_to_letter(number):
    n = number + 65
    return chr(n)

#counts the frequency of each letter A-Z in a given text
def count_letters(text:str):
    list = []
    for i in range(26):
        list.append(text.count(chr(i + 65)))
    return list

#returns the index of the biggest element in a given list
def most_common_letter(list):
    return list.index(max(list))

#calculates the difference between two numbers modulo 26
def calculate_key(index, common_letter):
    key = (index - (ord(common_letter)-65)) % 26
    return key

#applies frequency analysis on a text to return the key used to encrypt it with additive cypher
def frequency_analysis(text):
    common_letter = 'E'
    frequency_letters = count_letters(text)
    index_most_common_letter = most_common_letter(frequency_letters)
    key = calculate_key(index_most_common_letter, common_letter)
    return key

