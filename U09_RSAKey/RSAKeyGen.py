import sys
import functions as func

def main():
    length = sys.argv[1]
    output_private = sys.argv[2]
    output_public = sys.argv[3]
    prime_file = sys.argv[4]

    keys, p, q = func.key_gen_RSA(int(length))

    func.write(output_public, str(keys[0]))
    func.write(output_private, str(keys[1]))
    func.write(prime_file, (str(p) + '\n' + str(q)))

    return

main()

