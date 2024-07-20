import random
import sys
import time
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverso_modular(a, p):
    g, x, _ = gcd_extendido(a, p)
    return x % p

def gcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = gcd_extendido(b % a, a)
    return g, x - (b // a) * y, y

def adicion_curva_eliptica(P, Q, a, p):
    if P == Q:
        lam = (3 * P[0] * P[0] + a) * inverso_modular(2 * P[1], p) % p
    else:
        lam = (Q[1] - P[1]) * inverso_modular(Q[0] - P[0], p) % p

    x3 = (lam * lam - P[0] - Q[0]) % p
    y3 = (lam * (P[0] - x3) - P[1]) % p

    return (x3, y3)

def multiplicacion_curva_eliptica(k, P, a, p):
    R = (0, 0)
    Q = P
    while k > 0:
        if k % 2 == 1:
            R = adicion_curva_eliptica(R, Q, a, p)
        Q = adicion_curva_eliptica(Q, Q, a, p)
        k //= 2
    return R

def ecm(n, B1=10000, B2=100000):
    while True:
        x = random.randint(1, n - 1)
        y = random.randint(1, n - 1)
        a = random.randint(1, n - 1)
        b = (y * y - x * x * x - a * x) % n

        if (4 * a * a * a + 27 * b * b) % n == 0:
            continue

        P = (x, y)
        for k in range(2, B1):
            P = multiplicacion_curva_eliptica(k, P, a, n)
            g = gcd(P[1], n)
            if 1 < g < n:
                return g


        for k in range(B1, B2):
            P = multiplicacion_curva_eliptica(k, P, a, n)
            g = gcd(P[1], n)
            if 1 < g < n:
                return g

# # Ejemplo de uso
# numero = 10403
# factor = ecm(numero)
# print(f"Un factor de {numero} es: {factor}")

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = ecm(line)
    fin = time.time()
    # print(f'{line} = [{factores}]')
    print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}\\\\")