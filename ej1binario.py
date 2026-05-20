import random
import time
import matplotlib.pyplot as plt

def busqueda_binaria(numeros, objetivo):
    
    izquierda = 0                     #1 op
    derecha = len(numeros) - 1        #1 op

    while izquierda <= derecha:       #log n
        medio = (izquierda + derecha) // 2   #1 op log n
        
        if numeros[medio] == objetivo:       #1 op
            return medio
        elif numeros[medio] < objetivo:      #1 op
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

tamaños = [100, 1000, 10000, 100000, 500000, 1000000]
tiempos = []

for tamaño in tamaños:
    numeros = list(range(tamaño))
    objetivo = int(random.randint(0, tamaño - 1))

    inicio = time.perf_counter()
    busqueda_binaria(numeros, objetivo)
    fin = time.perf_counter()

    tiempos.append(fin - inicio)
    print(f"tiempo para {tamaño} numeros: {fin - inicio} segundos")

plt.plot(tamaños, tiempos, marker='o')
plt.xlabel("Cantidad de Elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Rendimiento de Busqueda Binaria - O(log n)")
plt.grid(True)
plt.show()