#Entrada
#La primera línea de entrada tiene un número entero n: el número de valores.
#La segunda línea tiene n números enteros x_1,x_2,\puntos,x_n.
#Salida
#Imprima un número entero: el número de valores distintos.

n = int(input())
lista_numeros = input().split()
if len(lista_numeros) == n:
    numeros_unicos = set(lista_numeros)
    print(len(numeros_unicos))

# lo que consiste este ejercicio es en definir el tamaño de una lista, y luego se ingresan los datos y la funcion set los transforma
# en un conjunto, el cual posteriormente LEN se asegura que la lista sea la correcta mediante el tamaño que se definio como primer numero
# de ingreso.
# Un ejemplo, pongan 5 (sera el tamaño que debe tener la lista inicial)
# luego, se definen los elementos que tendra esa lista, tienen que ser obligatoriamente 5
# y luego internamente la funcion numeros unicos logra procesar los elementos y los convierte en un set unico sin duplicados
# es decir, si usamos una lista de 2, 3, 3, 2, 3. La funcion set evita los duplicados y los transforma en 2, 3. Siendo asi 2 elementos
# los cuales LEN cuenta y arroja 2
