import sys


def calculo():
  # Leemos toda la entrada que manda el juez de golpe
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
  MOD = 1_000_000_007

  resultados = []
  idx = 1
  for _ in range(n):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    idx += 2
    resultados.append(str(pow(a, b, MOD)))

  # Imprimimos todo de un solo golpe
  print("\n".join(resultados))


if __name__ == "__main__":
  calculo()