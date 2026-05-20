import random
import time
import matplotlib.pyplot as plt

def multiplicacion_matrices(matriz_a, matriz_b, n):
    resultado = [[0] * n for _ in range(n)]  #crea matriz n×n llena de ceros, n operaciones
    
    for i in range(n):            #recorre la fila segun n
        for j in range(n):        #recorre la columna n veces cada i → n² 
            for k in range(n):    #suma n cada i,j → n³
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]  #2 ops
    
    return resultado             
tamaños = [10, 50, 100, 200, 300]
tiempos = []
for tamaño in tamaños:
    matriz_a = [[random.randint(0, 10) for _ in range(tamaño)] for _ in range(tamaño)]
    matriz_b = [[random.randint(0, 10) for _ in range(tamaño)] for _ in range(tamaño)]
    inicio = time.time()
    multiplicacion_matrices(matriz_a, matriz_b, tamaño)
    fin = time.time()
    tiempos.append(fin - inicio)
    print(f"tiempo para matriz {tamaño}x{tamaño}: {fin - inicio:.6f} segundos")
plt.plot(tamaños, tiempos, marker='o')
plt.xlabel("Dimension de la Matriz (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Multiplicacion de Matrices - O(n³)")
plt.grid(True)
plt.show()