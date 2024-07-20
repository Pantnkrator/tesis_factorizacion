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

x, a, m = map(int, input().split())
print(f'{x}^{a} % {m} = {mod_exp(x, a, m)}')