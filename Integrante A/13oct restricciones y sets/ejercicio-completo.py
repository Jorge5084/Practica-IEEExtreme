#Entrada
#La primera línea de entrada tiene un número entero n: el número de valores.
#La segunda línea tiene n números enteros x_1,x_2,\puntos,x_n.
#Salida
#Imprima un número entero: el número de valores distintos.

n = int(input("ingrese sus valores en enteros: "))
numero = set(input().split())
print(len(numero))

# lo que connsiste en mostrar este reto es la cantidad de veces en las que un set puede tardar en contar un primer valor
# si usamos 10 como ingreso, al definir 5 valores unicos como set, de forma progresiva y lineal se contaran las veces que intenta llegar
# hasta 10, por tanto en el ejercicio si toman mi ejemplo lo hara 3 veces, ese seria mi resultado
# prueben esto
# primer ingreso: 10 / Segundos ingresos del set: 2, 3, 3, 4, 5 (debe de dar 3)

