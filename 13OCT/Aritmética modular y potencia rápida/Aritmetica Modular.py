
# Usamos aritmetica modular para calcular los puntos de un combate en un juego.
# y nos ahorramos hacer un reccorido de todos los combates, ya que el patrón se repite cada 4 combates.

def calcular (combate):
    MOD = 1_000_000_007
    indice = (combate % 4)
    if indice == 0:
        puntos = (((combate // 4) * 85) + 5) % MOD
    elif  indice == 1:
        puntos = (((combate // 4) * 85) + 15) % MOD
    elif  indice == 2:
        puntos = (((combate // 4) * 85) + 35) % MOD
    elif  indice == 3:
        puntos = (((combate // 4) * 85) + 85) % MOD
    
    return(indice, puntos)

print(calcular(33))