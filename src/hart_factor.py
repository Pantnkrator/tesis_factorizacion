import sys
import time
import math

def factorizacion_hart(n):
    if n % 2 == 0:
        return (2, n // 2)

    def isqrt(x):
        return int(math.isqrt(x))

    for k in range(1, isqrt(2 * isqrt(n)) + 1):
        a = isqrt(k * n)
        b2 = a * a - k * n
        if b2 >= 0:
            b = int(math.isqrt(b2))
            if b * b == b2:
                gcd_k_n = math.gcd(k, n)
                if gcd_k_n == 1:
                    return (a - b, a + b)
                else:
                    return (gcd_k_n, n // gcd_k_n)
    return None

def mod_exp(base, exponente, modulo):
    resultado = 1
    base = base % modulo
    while exponente > 0:
        # print(f'{base} -> {exponente} -> {resultado}')
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo

    return resultado
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def hart_factorization(n, l):
    s = 1
    t = 1
    for i in range(1, l):
        s = math.ceil(math.sqrt(n*i))
        m = mod_exp(s, 2, n)
        t = math.isqrt(m)
        if t*t == m:
            break
    return gcd(s-t, n)


# print(hart_factors(5959))
for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    # factores = factorizacion_hart(line)
    factores = hart_factorization(line, line)
    fin = time.time()
    print(f'{line} = [{factores}]')
    # print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}")