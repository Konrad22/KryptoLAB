import math as m
import functions as func

#adds a string made up of '0' of the lenght of x to a string <message>
def add_x_bytes(message, x):
    zero_bytes = [0]*x
    return message + zero_bytes

#partitions a list <message> into lists that contain 16 bytes (128bit) each
#each element of the list <message> is a byte (8bit)
def block_partition_128(message):
    l = len(message)
    partitions_number = m.ceil(l/16)
    b = l/16
    if partitions_number > b:
        message = add_x_bytes(message, 16*partitions_number - l)
    partitions = [None]*partitions_number
    for i in range(partitions_number):
        partitions[i] = message[i*16: (i+1)*16]
    return partitions

#encrypts a bitstring using the ECB block cypher mode of operation
def ECB_encrypt(plain_text, key, encryption):             
    partitions = block_partition_128(plain_text)
    encrypted_partitions = [None]*len(partitions)
    for i in range(len(partitions)):
        encrypted_partitions[i] = encryption(partitions[i], key)
    encrypted_text = ''
    for partition in encrypted_partitions:
        encrypted_text = encrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return encrypted_text

#decrypts a bitstring using the ECB block cypher mode of operation
def ECB_decrypt(cypher_text, key, decryption):             
    partitions = block_partition_128(cypher_text)
    decrypted_partitions = [None]*len(partitions)
    for i in range(len(partitions)):
        decrypted_partitions[i] = decryption(partitions[i], key)
    decrypted_text = ''
    for partition in decrypted_partitions:
        decrypted_text = decrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return decrypted_text

#encrypts a bitstring using the CBC block cypher mode of operation
def CBC_encrypt(plain_text, key, encryption, initial_vector):
    partitions = block_partition_128(plain_text)
    partitions[0] = encryption(func.XOR_list(partitions[0], initial_vector), key)
    j = len(partitions)
    if j > 1:
        for i in range(1, j):
            partitions[i+1] = encryption(func.XOR_list(partitions[i], partitions[i+1]), key)
    encrypted_text = ''
    for partition in partitions:
        encrypted_text = encrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return encrypted_text

#decrypts a bitstring using the CBC block cypher mode of operation
def CBC_decrypt(cypher_text, key, decryption, initial_vector):          
    partitions = block_partition_128(cypher_text)
    j = len(partitions)
    if j > 1:
        for i in range(1, j):
            partitions[j-i-1] = func.XOR_list(decryption(partitions[j-i-1], key), partitions[j-i-2])
    partitions[0] = func.XOR_list(decryption(partitions[0], key), initial_vector)
    decrypted_text = ''
    for partition in partitions:
        decrypted_text = decrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return decrypted_text

#encrypts a bitstring using the OFB block cypher mode of operation
def OFB_encrypt(plain_text, key, encryption, vector):
    partitions = block_partition_128(plain_text)
    encrypted_vector = encryption(vector, key)
    for i in range(len(partitions)):
        partitions[i] = func.XOR_list(partitions[i], encrypted_vector)
        encrypted_vector = encryption(encrypted_vector, key)
    encrypted_text = ''
    for partition in partitions:
        encrypted_text = encrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return encrypted_text

#decrypts a bitstring using the OFB block cypher mode of operation
def OFB_decrypt(cypher_text, key, encryption, vector):
    partitions = block_partition_128(cypher_text)
    encrypted_vector = encryption(vector, key)
    for i in range(len(partitions)):
        partitions[i] = func.XOR_list(partitions[i], encrypted_vector)
        encrypted_vector = encryption(encrypted_vector, key)
    decrypted_text = ''
    for partition in partitions:
        decrypted_text = decrypted_text + ' '.join(func.int_list_to_hex(partition)) + ' '
    return decrypted_text

#encrypts a bitstring using the CTR block cypher mode of operation
def CTR_encrypt(plain_text, key, encryption):
    partitions = block_partition_128(plain_text)
    encrypted_text = ''
    for i in range(len(partitions)):
        counter = (func.int_to_hex(i % (2**128))).zfill(32)
        counter_as_list = [None]*16
        for j in range(16):
            counter_as_list[j] = func.hex_to_int(counter[2*j:2*j+2])
        encrypted_text = encrypted_text + ' '.join(func.int_list_to_hex(func.XOR_list(encryption(counter_as_list, key), partitions[i]))) + ' '
    return encrypted_text

#decrypts a bitstring using the CTR block cypher mode of operation
def CTR_decrypt(cypher_text, key, encryption):
    partitions = block_partition_128(cypher_text)
    decrypted_text = ''
    for i in range(len(partitions)):
        counter = (func.int_to_hex(i % (2**128))).zfill(32)
        counter_as_list = [None]*16
        for j in range(16):
            counter_as_list[j] = func.hex_to_int(counter[2*j:2*j+2])
        decrypted_text = decrypted_text + ' '.join(func.int_list_to_hex(func.XOR_list(encryption(counter_as_list, key), partitions[i]))) + ' '
    return decrypted_text