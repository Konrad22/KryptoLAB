import functions as func
import sys

def main():
    text = sys.argv[1]
    key = int(sys.argv[2])
    output = sys.argv[3]
    f = func.read(text)
    f = func.additive_chiffre_text_k(f,key)
    func.write(output, f)

main()