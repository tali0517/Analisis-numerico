#!/home/salzatec1/miniconda3/bin/python

from sustreg import sustreg
from sustprog import sustprog
import cmath
import numpy as np

def cholesky(A, b):
    n = np.array(A.shape[0])
    L = np.eye(n)
    U = np.eye(n)
    #L = L.astype(complex)

    for i in range(0, n-1):
        L[i][i] = np.sqrt(A[i][i] - L[i, 0:i].dot( np.matrix.transpose(U[0:i,i])))
        U[i][i] = L[i][i]
        

        for j in range(i+1, n):
            L[j][i] = np.divide((A[j][i] - L[j, 0:i].dot( np.matrix.transpose(U[0:i,i]))), U[i][i])

        for j in range(i+1, n):
            U[i][j] = np.divide((A[i][j] - L[i, 0:i].dot( np.matrix.transpose(U[0:i,j]))), L[i][i])

    L[n-1][n-1] = np.sqrt(A[n-1][n-1] - L[n-1, 0:n-1].dot( np.matrix.transpose(U[0:n-1,n-1]))) # Todavia no encuentro que hacer si la raiz es negativa
    # Funciona bien sin raices negativas
    U[n-1][n-1] = L[n-1][n-1]
    z= sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))
    return x

def main():
    #A = np.array(([3, 1, 1],
    #            [2, 3, 1],
    #            [4, -3, 1]))
    #b = np.array([0.5, 1, 0])
    A = np.array(([4, -1, 0, 3],
                  [1, 15.5, 3, 8],
                  [0, -1.3, -4, 1.1],
                  [14, 5, -2, 30]))
    b = np.array([1, 1, 1, 1])

    x = cholesky(A, b)
    print("X:\n", x)


if __name__=="__main__":
    main()
