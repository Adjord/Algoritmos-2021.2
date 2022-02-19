import numpy as np


def multiplicaMatrizes(matriz1, matriz2):
    matriz3 = np.empty(len(matriz1), int)
    for i in range(len(matriz1)):
        matriz3[i] = matriz1[i] * matriz2[i]
    return matriz3


def multiplicaMatrizesContadorInstrucoes(matriz1, matriz2):
    count = 0
    matriz3 = np.empty(len(matriz1), int)
    count += 1
    for i in range(len(matriz1)):
        count += 1
        matriz3[i] = matriz1[i] * matriz2[i]
        count += 1
    count += 1
    return count
