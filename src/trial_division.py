import sys
import time
def factorizar_por_divisiones_sucesivas(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores


def divisiones_sucesivas(n):
    factores = []
    while n % 2 == 0:
        factores.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n //= i
    if n > 2:
        factores.append(n)

    return factores

for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = factorizar_por_divisiones_sucesivas(line)
    # factores = divisiones_sucesivas(line)
    fin = time.time()
    print(f"{line} & {'{:.{}f}'.format((fin - inicio) * 1000, 3)} & {factores}\\\\")
    # print(f"{line} = {factores}")
    # print(f"{(fin-inicio)*1000}")
