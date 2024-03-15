import sys
import functions as func

def main():
    bitlength = sys.argv[1]
    func.Diffie_Hellman_key_exchange(int(bitlength))
    return

main()