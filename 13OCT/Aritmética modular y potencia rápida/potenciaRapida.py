base = 4
exponente = 7
MOD = 1_000_000_007

resultado = pow(base, exponente, MOD)

print(resultado)  # 16384

#por dentro pow:
def potencia_rapida(base, exponente, mod):
    resultado = 1

    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % mod

        base = (base * base) % mod
        exponente //= 2

    return resultado % mod