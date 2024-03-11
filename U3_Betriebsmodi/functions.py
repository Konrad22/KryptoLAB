import math as m

#adds a string made up of '0' of the lenght of x to a string <message>
def add_x_bits(message, x:int):
    return message + x*'0'

#partitions a string <message> into blocks of lenght <t>
def t_block_partition(message, t:int):
    l = len(message)
    a = m.ceil(l/t)
    b = l/t
    partitions_number = a
    if a > b:
        message = add_x_bits(message, t*partitions_number - l)
    partitions = []
    for i in range(partitions_number):
        if i == partitions_number:
            partitions.append(message[(i - 1)*t, l - 1])
            break
        partitions.append(message[(i - 1)*t, i*t - 1])
    return partitions

#partitions a string <message> into blocks of lenght 64
def block_partition_sixtyfour(message):
    return t_block_partition(message, 64)

#encrypts a bitstring using the ECB block cypher mode of operation, with blocklenght being a variable <t>
def ECB_encrypt(plain_text, t:int, encryption):             
    partitions = t_block_partition(plain_text, t)
    encrypted_partitions = encryption(partitions)
    encrypted_text = ''
    for partition in encrypted_partitions:
        encrypted_text =+ partition
    return encrypted_text

#decrypts a bitstring using the ECB block cypher mode of operation, with blocklenght being a variable <t>
def ECB_decrypt(cypher_text, t:int, decryption):             
    partitions = t_block_partition(cypher_text, t)
    decrypted_partitions = decryption(partitions)
    decrypted_text = ''
    for partition in decrypted_partitions:
        decrypted_text =+ partition
    return decrypted_text

#encrypts a bitstring using the CBC block cypher mode of operation, with blocklenght being a variable <t>
def CBC_encrypt(plain_text, t, encryption, vector):
    partitions = t_block_partition(plain_text, t)
    partitions[0] = encryption(partitions[0] ^ vector)
    for i in range(len(partitions)):
        partitions[i+1] = encryption(partitions[i] ^ partitions[i+1])
    encrypted_text = ''
    for partition in partitions:
        encrypted_text =+ partition
    return encrypted_text

#decrypts a bitstring using the CBC block cypher mode of operation, with blocklenght being a variable <t>
def CBC_decrypt(cypher_text, t, decryption, vector):          
    partitions = t_block_partition(cypher_text, t)
    j = len(partitions)
    for i in range(j):
        partitions[j-i] = decryption(partitions[j-i]) ^ partitions[j-i-1]
    partitions[0] = decryption(partitions[0]) ^ vector
    for partition in partitions:
        decrypted_text =+ partition
    return decrypted_text

#encrypts a bitstring using the OFB block cypher mode of operation, with blocklenght being a variable <t>
def OFB_encrypt(plain_text, t, encryption, vector):
    partitions = t_block_partition(plain_text, t)
    encrypted_vector = encryption(vector)
    for i in range(len(partitions)):
        partitions[i] = partitions[i] ^ encrypted_vector
        encrypted_vector = encryption(encrypted_vector)
    for partition in partitions:
        encrypted_text =+ partition
    return encrypted_text

#decrypts a bitstring using the OFB block cypher mode of operation, with blocklenght being a variable <t>
def OFB_decrypt(cypher_text, t, encryption, vector):
    partitions = t_block_partition(cypher_text, t)
    encrypted_vector = encryption(vector)
    for i in range(len(partitions)):
        partitions[i] = partitions[i] ^ encrypted_vector
        encrypted_vector = encryption(encrypted_vector)
    for partition in partitions:
        decrypted_text =+ partition
    return decrypted_text

#encrypts a bitstring using the CTR block cypher mode of operation, with blocklenght being a variable <t>
def CTR_encrypt(plain_text, t, encryption):
    partitions = t_block_partition(plain_text, t)
    encrypted_text = ''
    for i in range(len(partitions)):
        j = i % 2**t
        encrypted_text =+ encryption(j) ^ partitions[j]
    return encrypted_text

#decrypts a bitstring using the CTR block cypher mode of operation, with blocklenght being a variable <t>
def CTR_decrypt(cypher_text, t, encryption):
    partitions = t_block_partition(cypher_text, t)
    decrypted_text = ''
    for i in range(len(partitions)):
        j = i % 2**t
        decrypted_text =+ encryption(j) ^ partitions[j]
    return decrypted_text