"""
Autómata unidimensional Regla 30: generación y visualización.
Este software genera y visualiza un autómata celular unidimensional utilizando
la regla 30. Su propósito es ilustrar cómo patrones simples evolucionan con el
tiempo a partir de una celda activa, facilitando el estudio de sistemas
complejos y proporcionando una herramienta educativa para entender la dinámica
de los autómatas celulares.
"""

import matplotlib.pyplot as plt
import numpy as np


def regla30(celdas):
    """Aplica la regla 30 a una fila de celdas."""
    return np.array(
        [
            (celdas[i-1] ^ (celdas[i] or celdas[i+1]))
            for i in range(1, len(celdas)-1)
        ],
        dtype=int
    )


def automata_unidimensional(size, generaciones):
    """Genera el autómata celular unidimensional."""
    celdas = np.zeros(size, dtype=int)
    celdas[size // 2] = 1  # Celda inicial activa
    evolucion = [celdas.copy()]
    for _ in range(generaciones):
        celdas = np.pad(celdas, (1, 1), mode='constant', constant_values=0)
        celdas = regla30(celdas)
        evolucion.append(celdas.copy())

    return np.array(evolucion, dtype=int)
# Parámetros


SIZE = 101  # Tamaño de la fila de celdas
GENERACIONES = 50  # Número de generaciones

# Generar y visualizar el autómata
resultado_evolucion = automata_unidimensional(SIZE, GENERACIONES)
plt.imshow(resultado_evolucion, cmap='binary', interpolation='none')
plt.title('Autómata Celular Unidimensional - Regla 30')
plt.show()
