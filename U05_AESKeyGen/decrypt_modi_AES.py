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
            decrypted_text = m.ECB_decrypt(text, keys, func.decrypt_AES_128_bitblock)
        case 'CBC':
            initial_vector = [0]*16
            decrypted_text = m.CBC_decrypt(text, keys, func.decrypt_AES_128_bitblock, initial_vector)
        case 'OFB':
            hex_vector = sys.argv[5].zfill(32)
            initial_vector = [None]*16
            for i in range(16):
                initial_vector[i] = func.hex_to_int(hex_vector[2*i:2*i+2])
            decrypted_text = m.OFB_decrypt(text, keys, func.encrypt_AES_128_bitblock, initial_vector)
        case 'CTR':
            decrypted_text = m.CTR_decrypt(text, keys, func.encrypt_AES_128_bitblock)
        case _:
            decrypted_text = ''
    
    func.write(output, decrypted_text)
main()

#requires that roundkey_0 is being handed over