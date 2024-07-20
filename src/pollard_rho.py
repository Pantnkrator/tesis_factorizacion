import sys
import time
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
def pollard_rho(n):
    if n % 2 == 0:
        return 2

    # x = random.randint(2, n - 1)
    x = 2
    y = x
    c = 1
    # c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (mod_exp(x, 2, n) + c + n) % n
        print(f'x={x}')
        y = (mod_exp(y, 2, n) + c + n) % n
        print(f'y={y}')
        y = (mod_exp(y, 2, n) + c + n) % n
        print(f'y={y}')
        d = gcd(abs(x - y), n)
        print(f'd={d}')
    if d == n:
        return pollard_rho(n)

    return d

# Ejemplo de uso
# n = 10403  # Número a factorizar
# factor = pollard_rho(n)
# print(f"Un factor de {n} es {factor}")

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = pollard_rho(line)
    fin = time.time()
    print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}")