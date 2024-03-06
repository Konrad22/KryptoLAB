import functions as func
import sys

def main():
    text = sys.argv[1]
    f = func.read(text)
    key = func.frequency_analysis(f)
    f = str(key) + '\n' + func.decrypt_additive_chiffre_text_k(f,key)
    func.write("Klartext.txt", f)

main()