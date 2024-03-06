import math as m

def add_x_bits(message, x:int):
    return message + x*'0'

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

def block_partition_sixtyfour(message):
    return t_block_partition(message, 64)

def identity_encryption(message):
    return message

def ECB_encrypt(plain, t:int, encryption):             
    partitions = t_block_partition(plain, t)
    encrypted_partitions = encryption(partitions)
    encrypted_text = ''
    for partition in encrypted_partitions:
        encrypted_text =+ partition
    return encrypted_text

def ECB_decrypt(cypher, t:int, decryption):             
    partitions = t_block_partition(cypher, t)
    decrypted_partitions = decryption(partitions)
    decrypted_text = ''
    for partition in decrypted_partitions:
        decrypted_text =+ partition
    return decrypted_text

def CBC_encrypt(plain, t, encryption, vector):
    partitions = t_block_partition(plain, t)
    partitions[0] = encryption(partitions[0] ^ vector)
    for i in range(len(partitions)):
        partitions[i+1] = encryption(partitions[i] ^ partitions[i+1])
    encrypted_text = ''
    for partition in partitions:
        encrypted_text =+ partition
    return encrypted_text

def CBC_decrypt(cypher, t, decryption, vector):          
    partitions = t_block_partition(cypher, t)
    j = len(partitions)
    for i in range(j):
        partitions[j-i] = decryption(partitions[j-i]) ^ partitions[j-i-1]
    partitions[0] = decryption(partitions[0]) ^ vector
    for partition in partitions:
        decrypted_text =+ partition
    return decrypted_text

def OFB_encrypt(plain, t, encryption, vector):
    partitions = t_block_partition(plain, t)
    encrypted_vector = encryption(vector)
    for i in range(len(partitions)):
        partitions[i] = partitions[i] ^ encrypted_vector
        encrypted_vector = encryption(encrypted_vector)
    for partition in partitions:
        encrypted_text =+ partition
    return encrypted_text
    
def OFB_decrypt(cypher, t, encryption, vector):
    partitions = t_block_partition(cypher, t)
    encrypted_vector = encryption(vector)
    for i in range(len(partitions)):
        partitions[i] = partitions[i] ^ encrypted_vector
        encrypted_vector = encryption(encrypted_vector)
    for partition in partitions:
        decrypted_text =+ partition
    return decrypted_text

def CTR_encrypt(plain, t, encryption):
    partitions = t_block_partition(plain, t)
    encrypted_text = ''
    for i in range(len(partitions)):
        j = i % 2**t
        encrypted_text =+ encryption(j) ^ partitions[j]
    return encrypted_text

def CTR_decrypt(cypher, t, encryption):
    partitions = t_block_partition(cypher, t)
    decrypted_text = ''
    for i in range(len(partitions)):
        j = i % 2**t
        decrypted_text =+ encryption(j) ^ partitions[j]
    return decrypted_text