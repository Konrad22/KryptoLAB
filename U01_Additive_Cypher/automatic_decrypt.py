import functions as func
import sys

def main():
    text = sys.argv[1]
    f = func.read(text)
    key = func.frequency_analysis(f)
    f = str(key) + '\n' + func.decrypt_additive_chypher_text_k(f,key)
    func.write("Klartext.txt", f)

main()

#Programm zum Entschlüsseln ohne bekanntem Schlüssel
#Ausführen des Programms wie gefordert:
#Kommandozeile:  [input.txt] [Schlüssel] [output.txt]
#Test Korrektheit: sampleEncrypted.txt, die Ausgabe 'Klartext.txt' enthält lesbaren Text,
#dann nochmal mit encrypt und dem in Klartext.txt gegebenen Schlüssel verschlüsselt und verglichen