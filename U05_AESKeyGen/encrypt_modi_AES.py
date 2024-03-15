import functions as func
import modi as m
import sys

def main():
    modi = sys.argv[1]
    input = sys.argv[2]
    file_roundkey_0 = sys.argv[3]
    output = sys.argv[4]

    keys = func.prepare_key(file_roundkey_0)
    text = func.prepare_text(input)
    
    match modi:
        case 'ECB':
            encrypted_text = m.ECB_encrypt(text, keys, func.encrypt_AES_128_bitblock)
        case 'CBC':
            initial_vector = [0]*16
            encrypted_text = m.CBC_encrypt(text, keys, func.encrypt_AES_128_bitblock, initial_vector)
        case 'OFB':
            hex_vector = sys.argv[5].zfill(32)
            initial_vector = [None]*16
            for i in range(16):
                initial_vector[i] = func.hex_to_int(hex_vector[2*i:2*i+2])
            encrypted_text = m.OFB_encrypt(text, keys, func.encrypt_AES_128_bitblock, initial_vector)
        case 'CTR':
            encrypted_text = m.CTR_encrypt(text, keys, func.encrypt_AES_128_bitblock)
        case _:
            encrypted_text = ''
    
    func.write(output, encrypted_text)

main()

#vector needs to be put as hex