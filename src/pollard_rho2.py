import sys
import time
import random
import math
import sympy

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    return d

def factorizar(n):
    if n <= 1:
        return []
    if sympy.isprime(n):
        return [n]
    factors = []
    while n > 1:
        if sympy.isprime(n):
            factors.append(n)
            break
        factor = pollard_rho(n)
        while n % factor == 0:
            factors.append(factor)
            n //= factor
    return factors

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = factorizar(line)
    fin = time.time()
    print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}\\\\")
    # print(f'{line} = {factores}')