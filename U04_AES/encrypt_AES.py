import functions as func
import sys

def main():
    input = sys.argv[1]
    key = sys.argv[2]
    output = sys.argv[3]
    text, keys = func.prepare_text_and_key(input, key)
    encrypted_text = func.encrypt_AES_128_bitblock(text, keys)
    func.write(output, encrypted_text)

main()