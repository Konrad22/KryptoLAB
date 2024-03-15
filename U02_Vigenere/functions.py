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

#encrypts a text <text> according to viginere with key <key>
def encrypt_text_key(text, key):
    e_text = ""
    counter = 0
    mod = len(key)
    for l in text:
        k = transform_letter_to_number(key[counter])
        if(ord(l)> 64 and ord(l) < 91):
            e_text += shift_letter_k(l,k)
            counter = (counter + 1) % mod
        else:
            e_text += l
    return e_text

#decrypts a text <text> according to viginere with key <key>
def decrypt_text_key(text, key):
    d_text = ""
    counter = 0
    mod = len(key)
    for l in text:
        k = -transform_letter_to_number(key[counter])
        if(ord(l)> 64 and ord(l) < 91):
            d_text += shift_letter_k(l,k)
            counter = (counter + 1) % mod
        else:
            d_text += l
    return d_text

#encrypts a letter of the alphabet A-Z <letter> with a key <key> using the additive cypher
def shift_letter_k(letter, key):
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

#calculates the index of coincidence of a text <text>
def index_of_coincidence_text(text):
    n = len(text)
    if n < 2:
        return 0
    ic = (1/(n*(n-1)))
    abs_freq = 0
    for i in range(26):
        abs_freq += text.count(transform_number_to_letter(i))*(text.count(transform_number_to_letter(i))-1)
    return ic * abs_freq


#removes symbols from the given text <text> that are not part of the allowed alphabet and splits the text into <n> partitions
def partition_text(text, n):
    list = []
    text = text.translate({ord(i): None for i in '., -ÄÖÜ'})
    for i in range(n):
        part_text = ""
        while i < len(text):
            part_text += text[i]
            i += n
        list.append(part_text)
    return list

#finds and counts how many divisors and how often a divisor the number <n> has, returns a list <count_divisors> containing the count
def get_and_count_divisors(count_divisors, n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            count_divisors[i-1] =+ 1
    count_divisors[n-1] =+ 1
    return count_divisors