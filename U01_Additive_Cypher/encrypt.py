import functions as func
import sys

def main():
    text = sys.argv[1]
    key = int(sys.argv[2])
    output = sys.argv[3]
    f = func.read(text)
    f = func.encrypt_additive_chiffre_text_k(f,key)
    func.write(output, f)

main()

#Programm zum Verschlüsseln
#Ausführen des Programms wie gefordert:
#Kommandozeile:  [input.txt] [Schlüssel] [output.txt]
#Test Korrektheit: Klartext_1.txt 7 Kryptotext_1.txt, und dann mit 
#Kryptotext_1_Key_7.txt verglichen