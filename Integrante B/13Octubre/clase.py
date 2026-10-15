# Ejemplo de un grafo
g = [
    [],        # ignoramos posición 0
    [2, 3],    # nodo 1 conecta con 2 y 3
    [1],       # nodo 2 conecta con 1
    [1, 4],    # nodo 3 conecta con 1 y 4
    [3]        # nodo 4 conecta con 3
]
print (g[3])


#Patron Minimo de Python
grid = ["..#", ".#.", "..."]
h, w = len(grid), len(grid[0])
vecinos = [(1,0),(-1,0),(0,1),(0,-1)]
for dr, dc in vecinos:
 nr, nc = 0 + dr, 0 + dc
 if 0 <= nr < h and 0 <= nc < w:
    print(nr, nc)

grid = ["..#", ".#.", "..."]

h, w = len(grid), len(grid[0])

vecinos = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

for dr, dc in vecinos:
    nr, nc = 0 + dr, 0 + dc

    if 0 <= nr < h and 0 <= nc < w:
        print(nr, nc)