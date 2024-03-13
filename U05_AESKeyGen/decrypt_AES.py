import functions as func
import sys

def main():
    modi = sys.argv[1]
    input = sys.argv[2]
    key = sys.argv[3]
    output = sys.argv[4]
    if (sys.argv[5] != None):
        initial_vector = sys.argv[5]
    text = func.read(input)
    keys = func.read(key)
    text, keys = func.prepare_text_and_key(text, keys)
    decrypted_text = func.encrypt_AES_128_bitblock(text, keys, modi)
    func.write(output, decrypted_text)

main()