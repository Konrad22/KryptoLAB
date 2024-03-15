import sys
import functions as func

def main():
    print()
    input = sys.argv[1]
    key_file = sys.argv[2]
    output = sys.argv[3]

    message = int(func.read(input))
    key, n = func.read(key_file).splitlines()

    encrypted_text = func.encrypt_RSA(message, int(key), int(n))
    
    func.write(output, str(encrypted_text))
    
    return

main()