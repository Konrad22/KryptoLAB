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