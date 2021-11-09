#!/home/salzatec1/miniconda3/bin/python

from sustreg import sustreg
from sustprog import sustprog
import numpy as np

def doolittle(A, b):
    n = np.array(A.shape[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(0, n-1):
        for j in range(i, n):
            print("U:\n", U)
            U[i][j] = A[i][j] - L[i, 0:i].dot(np.matrix.transpose(U[0:i,j]))

        for j in range(i+1, n):
            print("L:\n", L)
            L[j][i] = np.divide((A[j][i] - L[j, 0:i].dot( np.matrix.transpose(U[0:i,i]))), U[i][i])

    print(L)
    print(U)
    U[n-1][n-1] = A[n-1][n-1] - L[n-1, 0:n-1].dot(np.matrix.transpose(U[0:n-1,n-1]))

    z= sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))
    return x

def main():
    A = np.array(([3, 1, 1],
                [2, 3, 1],
                [4, -3, 1]))
    b = np.array([0.5, 1, 0])
    x = doolittle(A, b)
    print("X:\n", x)


if __name__=="__main__":
    main()
