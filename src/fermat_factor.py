import sys
import time
import math

import math

def factorizacion_fermat(n):
    if n % 2 == 0:
        return (2, n // 2)

    a = math.ceil(math.sqrt(n))
    b2 = a * a - n

    while not es_cuadrado_perfecto(b2):
        a += 1
        b2 = a * a - n

    b = int(math.sqrt(b2))
    return (a - b, a + b)

def es_cuadrado_perfecto(x):
    s = int(math.isqrt(x))
    return s * s == x

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = factorizacion_fermat(line)
    fin = time.time()
    # print(f'{line} = {list(factores)}')
    print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}\\\\")