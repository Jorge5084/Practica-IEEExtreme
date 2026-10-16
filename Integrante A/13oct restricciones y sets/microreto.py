#Dada [7,7,2,4,2,9], calcula el número de valores distintos primero con dos bucles y luego con set.
#Autocomprobación: Resultado esperado: 4; explica diferencia entre O(n²) y O(n) esperado.

# Dos bucles
bucle1 =  [7,7,2,4,2,9]
for i in bucle1:
    for i2 in bucle1:
        print(i, i2)


# Set
bucle1 = [7,7,2,4,2,9]
datos_unicos = set(bucle1)
print(len(datos_unicos))

#Diferencias: O(n²) itera el doble de veces los valores por cada recorrido mientras que con O(n) se hace de forma mas directa

