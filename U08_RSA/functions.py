#opens file <filename>, reads text of the file into a variable, closes file, returns variable
def read(filename):
    f = open(filename, "r")
    t = f.read()
    f.close()
    return t

#opens file <filename>, writes text <text> into the file, closes file
def write(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

#calculates (<x> ** <m>) mod <n>
def power_mod(x, m, n):
    y = 1
    m_bin = bin(m).lstrip('0b')
    r = len(m_bin)
    for i in range(r):
        if m_bin[r - i - 1] == '1':
            y = (y*x) % n
        x = (x*x) % n
    return y

#en-/decrypts a decimal number <message> according to RSA depending on whether public or private <key> is used
def encrypt_RSA(message, key, n):
    y = power_mod(message, key, n)
    return y

