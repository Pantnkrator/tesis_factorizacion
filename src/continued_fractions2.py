import sys
import time
import math
from decimal import Decimal, getcontext

getcontext().prec = 50


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fraccion_continua_sqrt(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return [a0]
    
    cf = []
    m = Decimal(0)
    d = Decimal(1)
    a = Decimal(a0)
    cf.append(a)
    
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        cf.append(a)
    # print(f'Terminos de la fraccion continua: {cf}')
    return cf

def convergentes(cf):
    h1, h2 = Decimal(1), Decimal(0)
    k1, k2 = Decimal(0), Decimal(1)
    convergentes_list = []
    
    for i in range(len(cf)):
        h = cf[i] * h1 + h2
        k = cf[i] * k1 + k2
        convergentes_list.append((h, k))
        h2, h1 = h1, h
        k2, k1 = k1, k
    # print(f'Convergentes: {convergentes_list}')
    return convergentes_list

def decimal_sqrt(d):
    return d.sqrt()

def factorizar_fracciones_continuas(n):
    cf = fraccion_continua_sqrt(n)
    convs = convergentes(cf)
    
    for h, k in convs:
        if k == 0:
            continue
        x = h
        y = (x * x - n) // k
        
        # if y >= 0 and decimal_sqrt(y) % 1 == 0:  # Verificar si la raíz cuadrada es un entero
        #     factor = gcd(x + int(decimal_sqrt(y)), n)
        #     if 1 < factor < n:
        #         return factor
            
        if y >= 0 and int(Decimal(math.isqrt(int(y)))) ** 2 == y:
            factor = gcd(x + int(Decimal(math.isqrt(int(y)))), n)
            if 1 < factor < n:
                return factor
        
        # if y >= 0 and int(math.isqrt(y)) ** 2 == y:
        #     factor = gcd(x + int(math.isqrt(y)), n)
        #     if 1 < factor < n:
        #         return factor
    
    return None

# Ejemplo de uso
# numero = 10403
# factor = factorize_using_cf(numero)
# if factor:
#     print(f"Un factor de {numero} es: {factor}")
# else:
#     print(f"No se encontró un factor para {numero}.")

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = factorizar_fracciones_continuas(line)
    fin = time.time()
    # print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}")
    print(f'{line} = [{factores}]')