import sys

def read(filename):
    f = open(filename, "r")
    t = f.read()
    f.close()
    return t

def write(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

def encrypt_additive_chiffre_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_chiffre_letter_k(l,key)
    return e_text

def decrypt_additive_chiffre_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_chiffre_letter_k(l,-key)
    return e_text

def additive_chiffre_letter_k(letter, key):
    if(ord(letter)> 64 and ord(letter) < 91):
        letter = transform_number_to_letter((transform_letter_to_number(letter) + key)%26)
    return letter

def transform_letter_to_number(letter):
    n = ord(letter)
    return n-65

def transform_number_to_letter(number):
    n = number + 65
    return chr(n)

def count_letters(text:str):
    list = []
    for i in range(26):
        list.append(text.count(chr(i + 65)))
    return list

def most_common_letter(list):
    return list.index(max(list))

def calculate_key(index, common_letter):
    key = (index - (ord(common_letter)-65)) % 26  
    return key

def frequency_analysis(text):
    common_letter = 'E'
    frequency_letters = count_letters(text)
    index_most_common_letter = most_common_letter(frequency_letters)
    key = calculate_key(index_most_common_letter, common_letter)
    return key

