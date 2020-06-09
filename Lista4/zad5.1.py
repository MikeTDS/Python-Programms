from cmath import exp
from math import pi
import numpy as np
from time import time
import random

class FastBigNum:
    def __init__(self, x):
        self.x = x
    def __mul__(self,y):
       a,b = prepare(self,y)
       return multiply(a,b)

    def __str__(self):
        return str(self.x)

def omega(k,n):
    return exp(-2j*k*pi/n)

def dft(x,n):
    return [sum(x[i]*omega(i*k,n) if i<len(x) else 0 for i in range(n)) for k in range(n)]

def idft(x,n):
    return [int(round(sum(x[i]*omega(-i*k,n) if i<len(x) else 0 for i in range(n)).real)/n) for k in range(n)]

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

def multiply(a,b):
    x1 = list(reversed([int(i) for i in a.x]))
    y1 = list(reversed([int(i) for i in b.x]))
    xa = dft(x1, 2*len(x1))
    ya = dft(y1, 2*len(y1))
    za = np.multiply(xa,ya)
    z = idft(za,len(za))
    temp = 0
    for i in range(len(z)):
        temp += z[i]*pow(10,i)
    return FastBigNum(str(temp))

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
