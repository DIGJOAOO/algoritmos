import random
import time
import matplotlib.pyplot as plt

def busqueda_lineal(numeros, objetivo):
    for numero in numeros:              #n
        if numero == objetivo:          #1 op
            return numeros.index(numero) #1 op
    return -1
tamaños = [100, 1000, 10000, 100000, 500000, 1000000]
tiempos = []
for tamaño in tamaños:
    numeros = list(range(tamaño))
    objetivo = int(random.randint(0, tamaño - 1))
    inicio = time.time()
    busqueda_lineal(numeros, objetivo)
    fin = time.time()
    tiempos.append(fin - inicio)
    print(f"tiempo para {tamaño} numeros: {fin - inicio} segundos")

plt.plot(tamaños, tiempos, marker='o')
plt.xlabel("Cantidad de Elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Rendimiento de Busqueda Lineal - O(n)")
plt.grid(True)
plt.show()