def gcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = gcd_extendido(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


# Ejemplo de uso
num1, num2 = map(int, input().split())
gcd, x, y = gcd_extendido(num1, num2)
# print(f"El GCD de {num1} y {num2} es {gcd}, con los coeficientes x = {x} y y = {y}")
print(f"gcd({num1}, {num2}) = {gcd}\nx = {x}\ny = {y}")
