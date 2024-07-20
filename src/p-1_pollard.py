import math
from math import gcd

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    for start in range(2, limit + 1):
        if sieve[start]:
            primes.append(start)
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    
    return primes

def modular_exponentiation(base, exponent, modulo):
    result = 1
    base = base % modulo  # Ensure base is smaller than modulo
    
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulo
        exponent = exponent >> 1
        base = (base * base) % modulo
    
    return result

def pollards_p_minus_1(n, B):
    a = 2  # A commonly used base
    
    # Get all primes up to B using the sieve of Eratosthenes
    primes = sieve_of_eratosthenes(B)
    
    # Calculate the product of primes raised to the highest power <= n
    M = 1
    for p in primes:
        e = math.floor(math.log(n) / math.log(p))
        M *= pow(p, e)
    
    # Calculate a^M mod n
    aM = modular_exponentiation(a, M, n)
    
    # Calculate gcd(a^M - 1, n)
    d = gcd(aM - 1, n)
    
    if 1 < d < n:
        return d
    else:
        return None

# Example usage
n = 1256132134125569  # Number to factor
B = 30000000  # Smoothness bound
factor = pollards_p_minus_1(n, B)
if factor:
    print(f"A factor of {n} is {factor}")
else:
    print("No non-trivial factor found with the given smoothness bound.")
