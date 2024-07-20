import random
import math

primos_file = open("primes.txt", "r")
data = primos_file.read()
primos_list = data.split("\n")
primos_list.pop()
primos_file.close()


def primos_aleatorios_menores_a(n):
    primos = list(map(int, primos_list))
    upper = binary_search(n, primos)
    for i in range(6, 23):
        number = 1
        fact = []
        while math.log10(number) < i:
            x = random.randint(0, upper)
            prime = primos[x]
            number = number * prime
            fact.append(prime)
        print(f'{number} = {fact}')


def binary_search(x, array):
    a = 0
    b = len(array)
    while(b-a > 1):
        c = math.floor((b+a)/2)
        if array[c] > x:
            b = c
        else:
            a = c
    return a


def dos_primos_mitad_digitos():
    primos = list(map(int, primos_list))
    for i in range(6, 18):
        lower = binary_search(pow(10, i/2), primos)
        upper = binary_search(pow(10, (i/2)+1), primos)
        n1 = random.randint(lower, upper+1)
        n2 = random.randint(lower, upper + 1)
        number = primos[n1] * primos[n2]
        fact = [primos[n1], primos[n2]]
        print(f'{number} = {fact}')


def dos_primos_cercanos():
    primos = list(map(int, primos_list))
    for i in range(6, 18):
        lower = binary_search(pow(10, i/2), primos)
        upper = binary_search(pow(10, (i/2)+1), primos)
        n1 = random.randint(lower, upper+1)
        n2 = n1 + random.randint(0, 100)*(-1**random.randint(0, 10))
        number = primos[n1] * primos[n2]
        fact = [primos[n1], primos[n2]]
        print(f'{number} = {fact}')


primos_aleatorios_menores_a(10000)
dos_primos_mitad_digitos()
dos_primos_cercanos()