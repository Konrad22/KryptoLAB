import functions as func
import sys

def main():
    text = sys.argv[1]
    key = -int(sys.argv[2])
    output = sys.argv[3]
    f = func.read(text)
    f = func.decrypt_additive_chiffre_text_k(f,key)
    func.write(output, f)

main()

#Programm zum Entschlüsseln mit bekanntem Schlüssel
#Ausführen des Programms wie gefordert:
#Kommandozeile:  [input.txt]
#Test Korrektheit: Kryptotext_1_Key_7.txt 7 Klartext_1_Key_7.txt, und dann mit 
#Klartext_1.txt verglichen