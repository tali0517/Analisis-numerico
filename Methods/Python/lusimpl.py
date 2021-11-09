#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg
from sustprog import sustprog

def lusimpl(A, b):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A
    M = M.astype('float')
    stack = []
    etapa = 0
    # Todas las columnas de A - 1
    for i in range(0, n - 1):
        print("Etapa", etapa)
        print(M)
        print()
        etapa += 1
        # Por cada columna iterar por cada fila debajo de la diagonal
        for j in range(i+1, n):
            if M[j][i] != 0:
                # Operacion de subfila
                L[j][i] = M[j][i]/M[i][i]
                M[j][i:n+1] = M[j][i:] - (M[j][i]/M[i][i])*M[i][i:]

        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]

    U[n-1][n-1] = M[n-1][n-1]

    print("Etapa", etapa)
    print(M, '\n')
    stack = np.array(stack, dtype=int).reshape(-1,2)
    # Sustitucion regresiva
    #print("Despues de aplicar sustitucion regresiva\n")
    z = sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))
    return x

def main():
    #size = 4
    #A = np.random.rand(size, size)
    #b = np.random.rand(size)
    #A = np.array(([2, -1, 0, 3], 
    #             [1, 0.5, 3, 8], 
    #             [0, 13, -2, 11], 
    #             [14, 5, -2, 3]))
    #b = np.array([1, 1, 1, 1])
    #A = np.array(([0, 0, 1],
    #            [4, 2, 1],
    #            [0.81, 0.9, 1]))
    #b = np.array([0.5, 1, 0])
    A = np.array(([3, 1, 1],
                [2, 3, 1],
                [4, 8, 1]))
    b = np.array([0.5, 1, 0])
    x = lusimpl(A, b)
    print("X:\n", x)


if __name__ == '__main__':
    main()
