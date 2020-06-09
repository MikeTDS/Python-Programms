from cmath import exp
from math import pi
import numpy as np
import math
from time import time
import random

class FastBigNum:
    def __init__(self, x):
        self.x = x
    def __mul__(self,y):
        a,b = prepare(self,y)
        a1,b1 = to_list(a.x,b.x)
        return multiply(a1,b1)

    def __str__(self):
        return str(self.x)

def omega(k,n):
    return exp(-2j*k*pi/n)

def dft(x):
    n = len(x)
    return [sum(x[i]*omega(i*k,n) if i<len(x) else 0 for i in range(n)) for k in range(n)]

def fft(x):
    n = len(x)
    if n <= 4:
        return dft(x)
    else:
        x_even = fft(x[::2])  
        x_odd = fft(x[1::2])
        om = np.exp(-2j*pi*np.arange(n)/n)
        x1 = x_even + x_odd * om[:n//2]
        x2 = x_even + x_odd * om[n//2:]
        res = np.concatenate([x1, x2])
    return res

def ifft(x):
    x_conj = np.conj(x)
    x = fft(x_conj)
    temp = np.conj(x)
    res = temp / len(x)
    return res

def prepare(a,b):
    lena = len(a.x)
    lenb = len(b.x)

    if lena < lenb:
        while len(a.x) != len(b.x):
            a.x = '0' + a.x
    if lenb < lena:
        while len(a.x) != len(b.x):
            b.x = '0' + b.x    

    return a,b

def to_list(a,b):
    length = len(a)
    a1 = list(reversed([int(i) for i in a]))
    b1 = list(reversed([int(i) for i in b]))
    a1 += [0 for i in range(length)]
    b1 += [0 for i in range(length)]
    while not math.log2(len(a1)).is_integer():
        a1.append(0)
    while not math.log2(len(b1)).is_integer():
        b1.append(0)
    return a1, b1

def multiply(x,y):
    xa = fft(x)
    ya = fft(y)
    za = np.multiply(xa,ya)
    z =  ifft(za)
    z = [int(round(i.real)) for i in z]
    temp = 0
    for i in range(len(z)):
        temp += z[i].real*pow(10,i)
    return FastBigNum(str(int(temp)))

def test_time():
    sizes = [1000,5000,10000]
    for size in sizes:
        A = ''.join([random.choice('0123456789') for i in range(size)])
        B = ''.join([random.choice('0123456789') for i in range(size)])
        a = FastBigNum(A)
        b = FastBigNum(B)
        start = time()
        a*b
        end = time() - start
        print(end)

def main():
    test_time()

if __name__ == "__main__":
    main()