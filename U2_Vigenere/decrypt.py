import functions as func
import sys

def main():
    text = sys.argv[1]
    key = sys.argv[2]
    output = sys.argv[3]
    f = func.read(text)
    f = func.decrypt_text_key(f,key)
    func.write(output, f)

main()

#Programm zum Verschlüsseln mit bekanntem Schlüssel
#Ausführen des Programms wie gefordert:
#Kommandozeile:  [input.txt] [Schlüssel] [output.txt]
#Test Korrektheit: Kryptotext_TAG TAG Klartext_Tag
#mit Klartext_1 verglichen