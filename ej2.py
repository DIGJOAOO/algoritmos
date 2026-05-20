import random
import time
import matplotlib.pyplot as plt

tiempos = []

def elementos_unicos(numeros):
    for i in range(len(numeros)):                 #n
        for x in range(i + 1, len(numeros)):      #n*(n-1)/2
            if numeros[i] == numeros[x]:          #1 op
                return False                      #1 op, opcional
    return True                                   

tamaños = [100, 500, 1000, 2000, 5000]
tiempos = []
for tamaño in tamaños:
    numeros = list(range(tamaño))
    inicio = time.time()
    elementos_unicos(numeros)
    fin = time.time()
    tiempos.append(fin - inicio)
    print(f"tiempo para {tamaño} numeros: {fin - inicio} segundos")
plt.plot(tamaños, tiempos, marker='o')
plt.xlabel("Cantidad de Elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Elementos Unicos - O(n²)")
plt.grid(True)
plt.show()
