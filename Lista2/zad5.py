import random
import os
import sys
from math import log as log

#Losowanie n-bitowej liczby
def generate_random_number(bits):
    digits = int(log(2)/log(10)*(bits))
    lr = 10**(digits - 1)
    ur = (10**digits) - 1
    return random.randrange(lr, ur)

#Miller-Rabin test (power, m_r_t, c_i_p)
def miller_rabin_test(d,n):
    a = 2 + random.randint(1, n-4)
    x = pow(a,d,n)

    if x == 1 or x == n-1:
        return True
    
    while d!=n-1:
        x = x**2 % n
        d *= 2

        if x == 1:
            return False
        if x == n-1:
            return True
    
    return False

def check_if_prime(n, k):

    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n-1
    while(d % 2 == 0):
        d //= 2
    
    for i in range(k):
        if(miller_rabin_test(d,n) == False):
            return False
    
    return True

#d*e przystaje 1 mod(phi)
def egcd(e, phi):
    if e == 0:
        return (phi, 0, 1)
    else:
        g, y, x = egcd(phi % e, e)
        return(g, x - (phi // e) * y, y)

def inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        return -1
    return x%phi

#Generowanie kluczy    
def generate_keys(bits):
    accuracy = 10000
    p = 10
    q = 10

    while(not check_if_prime(p,accuracy)):
        p = generate_random_number(bits)
    while(not check_if_prime(q,accuracy)):
        q = generate_random_number(bits)
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    d = inverse(e, phi)

    return(e, d, n)

#Szyfrowanie:
def encrypt(e, n, message):
    cipher = 0
    for i in message:
        cipher = (cipher << 8) + ord(i)
    return pow(cipher, e, n)

#Odszyfrowanie:
def decrypt(d, n, cipher):
    message = ''
    temp = pow(cipher, d, n)
    while temp > 0:
        message = chr(temp & 0xFF) + message
        temp >>= 8
    return message

def main():  
    if sys.argv[1] == '--gen-keys':
        d = -1
        while d == -1:
            (e, d, n) = generate_keys(int(sys.argv[2]))
        with open('key.pub', 'w+') as f1:
            f1.write(str(e) + ' ' + str(n) + '\n')
        with open('key.prv', 'w+') as f2:
            f2.write(str(d) + ' ' + str(n) + '\n')

    elif sys.argv[1] == '--encrypt':
        message = sys.argv[2]

        with open('key.pub') as file:
            temp = file.read()

        keys = temp.split()
        e = int(keys[0])
        n = int(keys[1])
        cipher = encrypt(e,n,message)
        print(cipher)

    elif sys.argv[1] == '--decrypt':
        cipher = int(sys.argv[2])
        with open('key.prv') as file:
            temp = file.read()

        keys = temp.split()
        d = int(keys[0])
        n = int(keys[1])
        message = decrypt(d,n,cipher)
        print(message)

if __name__ == '__main__':
    main()