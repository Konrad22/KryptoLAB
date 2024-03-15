import random

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
        if m_bin[- i - 1] == '1':
            y = (y*x) % n
        x = (x*x) % n
    return y

#en-/decrypts a decimal number <message> according to RSA depending on whether public or private <key> is used
def encrypt_RSA(message, key, n):
    y = power_mod(message, key, n)
    return y

#generates a prime with the approximate length of the bits
def generate_prime(bits):
	z = random.randrange(2**(bits - 1), 2** bits)
	x = 30 * z
	primes = [1, 7, 11, 13, 17, 19, 23, 29]
	offset = 0

	while not miller_rabin_multiple(x, 20):
		x = x + primes[offset % len(primes)] + 30 * (offset // len(primes))
		offset += 1

	return x

#Miller-Rabin-test to check if <n> is prime, returns True if prime
#chance for false return of 'False' is 0, and chance for false return of 'True' is <= 1/4
def miller_rabin(n):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False
    m, k = find_m_k(n)
    a = random.randrange(2, n)
    b = power_mod(a, m, n)
    if b%n == 1:
        return True
    for i in range(k):
        if (b%n) == (n-1):
            return True
        else:
            b = power_mod(b, 2, n)
    return False

#runs the Miller-Rabin-test <times> to lower the likelyhood of a false answer
def miller_rabin_multiple(x, times):
    for i in range(times):
        if miller_rabin(x) == False:
            return False
    return True

#finds m, k such that n - 1 = 2^k * m
def find_m_k(n):
    m = (n - 1) // 2
    k = 1
    while m % 2 == 0:
        m //= 2
        k += 1
    return int(m), k

#generates a key pair for RSA and also returns the primes used
def key_gen_RSA(keylength):
    p = generate_prime(keylength)
    q = generate_prime(keylength)
    n = p*q
    phi_n = phi(p,q)
    e = random.randrange(q//2, 8*q)
    while not ggT_extended(e, phi_n):
        e = random.randrange(q//2, 8*q)
    d = ggT_extended(e, phi_n)[1] % n
    keys = [[e, n], [d, n]] 
    return keys, p, q

#calculates phi(p*q) for p and q being prime
def phi(p,q):
    return (p-1) * (q-1)

#calculates the extended euklid algorithm
def ggT_extended(a, b):
    k = 0
    r = [a, b] 
    s = [1, 0]
    t = [0, 1]
    while not r[k + 1] == 0:
        k = k + 1
        q = r[k-1]/r[k]
        r.append(r[k-1] - q * r[k])
        s.append(s[k-1] - q * s[k])
        t.append(t[k-1] - q * t[k])
    return r[k], s[k], t[k]

#generates an int <e> with ggT(e, phi) = 1
def generate_e(phi):
    if ggT_extended(2**16 + 1, phi)[0]:
        return 2**16 + 1
