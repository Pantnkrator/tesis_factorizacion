import random
import math
import sys
import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def modular_inverse(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return None
    if t < 0:
        t = t + n
    return t


class EllipticCurve:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def add_points(self, P, Q):
        if P == (0, 0):
            return Q
        if Q == (0, 0):
            return P
        if P == Q:
            lamb = (3 * P[0] ** 2 + self.a) * modular_inverse(2 * P[1], self.n) % self.n
        else:
            lamb = (Q[1] - P[1]) * modular_inverse(Q[0] - P[0], self.n) % self.n
        x3 = (lamb ** 2 - P[0] - Q[0]) % self.n
        y3 = (lamb * (P[0] - x3) - P[1]) % self.n
        return x3, y3

    def multiply_point(self, k, P):
        R = (0, 0)
        Q = P
        while k > 0:
            if k % 2 == 1:
                R = self.add_points(R, Q)
            Q = self.add_points(Q, Q)
            k //= 2
        return R


def factorize_ecm(n, B1=10000):
    while True:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        curve = EllipticCurve(a, b, n)
        P = (random.randint(0, n - 1), random.randint(0, n - 1))
        d = gcd(4 * a ** 3 + 27 * b ** 2, n)
        if 1 < d < n:
            return d
        Q = P
        for q in range(2, B1 + 1):
            Q = curve.multiply_point(q, Q)
            d = gcd(Q[1], n)
            if 1 < d < n:
                return d
for line in sys.stdin:
    line = int(line.strip())
    inicio = time.time()
    factores = factorize_ecm(line)
    fin = time.time()
    print(f"{line} & {'{:.{}f}'.format((fin-inicio)*1000, 3)} & {factores}")