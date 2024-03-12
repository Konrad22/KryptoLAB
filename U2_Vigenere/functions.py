import sys

def read(filename):
    f = open(filename, "r")
    t = f.read()
    f.close()
    return t
#Datei öffnen, Text in der Datei als Variable einleisen, Datei schließen

def write(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()
    #Datei öffnen, Inhalt der Variable in die Datei schreiben, Datei schließen

def encrypt_text_key(text, key):
    #Schlüssel wird als Liste übergeben
    e_text = ""
    counter = 0
    mod = len(key)
    for l in text:
        k = transform_letter_to_number(key[counter])
        #Schlüssel für den jeweiligen zu verschlüsselnden Buchstaben ist Element der Schlüsselliste
        if(ord(l)> 64 and ord(l) < 91):
            #Zeichen außerhalb des Alphabet sollen übersprungen werden und
            #und kein Zeichen des Schlüssels verbrauchen
            e_text += shift_letter_k(l,k)
            counter = (counter + 1) % mod
            #Schlüsselelement ist 'verbraucht'
        else:
            e_text += l
            #Zeichen kann nicht verschlüsselt werden, bleibt unverändert
    return e_text

def decrypt_text_key(text, key):
    d_text = ""
    counter = 0
    mod = len(key)
    for l in text:
        k = -transform_letter_to_number(key[counter])
        if(ord(l)> 64 and ord(l) < 91):
            #Zeichen außerhalb des Alphabet sollen übersprungen werden und
            #und kein Zeichen des Schlüssels verbrauchen
            d_text += shift_letter_k(l,k)
            counter = (counter + 1) % mod
        else:
            d_text += l
    return d_text
#analog zum Verschlüsseln, nur mit invertiertem Schlüssel

def shift_letter_k(letter, key):
    letter = transform_number_to_letter((transform_letter_to_number(letter) + key)%26)
    return letter
#identisch zu 'additive_chiffre_letter_k' aus Übung 1, nur das hier auf einer höheren Ebene
#Zeichen die nicht im Alphabet enthalten sind, abgefangen werden

def transform_letter_to_number(letter):
    n = ord(letter)
    return n-65
#ordnet den Buchstaben A-Z die Zahlen 0-25 zu, damit es intuitiver ist

def transform_number_to_letter(number):
    n = number + 65
    return chr(n)
#transformiert die Zahlen 0-25 wieder zu den Buchstaben A-Z

def count_letters(text:str):
    list = []
    for i in range(26):
        list.append(text.count(chr(i + 65)))
    #zählt wie oft alle Buchstaben jeweils in einem Text vorkommen
    return list

def most_common_letter(list):
    return list.index(max(list))
#gibt den Index des größten Elements der Liste aus

def calculate_key(index, common_letter):
    key = (index - (ord(common_letter)-65)) % 26
    #gibt aus wie groß der Abstand zwischen der Zahl index und der Zahlrepräsentation des gegeben Wortes ist
    return key

def frequency_analysis(text):
    common_letter = 'E'
    frequency_letters = count_letters(text)
    index_most_common_letter = most_common_letter(frequency_letters)
    key = calculate_key(index_most_common_letter, common_letter)
    return key
#Frequency analysis mit den vorherigen drei Bausteinen

def index_of_coincidence_text(text):
    n = len(text)
    if n < 2:
        return 0
    ic = (1/(n*(n-1)))
    abs_freq = 0
    for i in range(26):
        abs_freq += text.count(transform_number_to_letter(i))*(text.count(transform_number_to_letter(i))-1)
    return ic * abs_freq

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

def sieve_list(list, n):
    sieve_list = []
    for i in range(len(list)):
        i = n
        sieve_list.append(list[i])
        i = i + n
    return sieve_list

def averaged_sieve_lists(list):
    averaged_sieve_list = []
    for i in range (len(list)):
        sieve_list_i = sieve_list(list, i)
        average_i = sum(sieve_list_i)/len(sieve_list_i)
        averaged_sieve_list.append(average_i)
    return averaged_sieve_list

def get_and_count_divisors(count_divisors, n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            count_divisors[i-1] =+ 1
    count_divisors[n-1] =+ 1
    return count_divisors

def likely_key_length(index_list):
    l = len(index_list)
    
    return