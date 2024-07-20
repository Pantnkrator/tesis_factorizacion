def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    
    for start in range(2, limit + 1):
        if sieve[start]:
            print(start)
            primes.append(start)
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    
    return primes


limite = 1000000000
primos = sieve_of_eratosthenes(limite)