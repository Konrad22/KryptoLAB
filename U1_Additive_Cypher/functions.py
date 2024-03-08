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

def encrypt_additive_chiffre_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_chiffre_letter_k(l,key)
        #verschlüsselter Text aus den einzeln verschlüsselten Buchstaben zusammengesetzt
    return e_text
    #verschlüsseln eines Textes mit Additiver Chiffre für Schlüssel k

def decrypt_additive_chiffre_text_k(text, key):
    e_text = ""
    for l in text:
        e_text += additive_chiffre_letter_k(l,-key)
        #entschlüsselter Text aus den einzeln entschlüsselten Buchstaben zusammengesetzt
    return e_text
    #entschlüsseln eines Textes mit Additiver Chiffre für Schlüssel k  

def additive_chiffre_letter_k(letter, key):
    if(ord(letter)> 64 and ord(letter) < 91):
        letter = transform_number_to_letter((transform_letter_to_number(letter) + key)%26)
    return letter
#nimmt einen Buchstaben des erlaubten Alphabets, und verschlüsselt ihn mit Additiver Chiffre für Schlüssel k

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

