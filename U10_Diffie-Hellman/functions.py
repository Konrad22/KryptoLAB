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

def Diffie_Hellman_key_exchange(bitlength):
    p, q = generate_primes(bitlength)
    print('Prime: ', p)
    g = calc_generator(p, q)
    print('\nGenerator: ', g)
    a = random.randint(2, p-1)
    b = random.randint(2, p-1)
    A = power_mod(g, a, p)
    calc_Alice = '\nA = ', g, '^' , a , ' mod ' , p , '\n' + 'A = ' , A
    print(calc_Alice)
    B = power_mod(g, a, p)
    calc_Bob = '\nB = ' , g , '^' , b , ' mod ' , p , '\n' + 'B = ' , B
    print(calc_Bob)
    shared_key = power_mod(A, b, p)
    print('\Shared key: ' , shared_key)
    return

#generates p and q, where p = 2 * q + 1
#because p = 2 * q + 1, we know that p - 1 = 2*q, meaning it only has the prime factors 2 and q
def generate_primes(bitlength):
    p = 1
    while not miller_rabin_multiple(p, 20):
        q = generate_prime(bitlength - 1)
        print(q)
        p = 2 * q + 1
    return p, q

#calculates a generator for a prim number <p> = 2 * <q> + 1
#because p = 2 * q + 1, we know that p - 1 = 2*q, meaning it only has the prime factors 2 and q
def calc_generator(p, q):
    m = p - 1
    a = 1
    while power_mod(a, m // 2, p) == 1 or power_mod(a, m // q, p) == 1:
        a = random.randrange(2, p)
    return a
    
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
    if b == 1 % n:
        return True
    for i in range(k):
        if b == -1 % n:
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

#finds m, k such that n - 1 = 2**k * m
def find_m_k(n):
    m = (n - 1) // 2
    k = 1
    while m % 2 == 0:
        m = m // 2
        k = k + 1
    return int(m), k

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