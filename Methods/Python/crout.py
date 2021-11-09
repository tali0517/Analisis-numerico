#!/home/salzatec1/miniconda3/bin/python

from sustreg import sustreg
from sustprog import sustprog
import numpy as np

def crout(A, b):
    n = np.array(A.shape[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(0, n-1):

        for j in range(i, n):
            L[j][i] = A[j][i] - L[j, 0:i].dot( np.matrix.transpose(U[0:i,i]))
            print("L:\n", L)

        for j in range(i+1, n):
            U[i][j] = np.divide((A[i][j] - L[i, 0:i].dot( np.matrix.transpose(U[0:i,j]))), L[i][i])
            print("U:\n", U)

    L[n-1][n-1] = A[n-1][n-1] - L[n-1, 0:n-1].dot( np.matrix.transpose(U[0:n-1,n-1]))
    print("L:\n", L)
    z= sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))

    return x

def main():
    A = np.array(([3, 1, 1],
                [2, 3, 1],
                [4, 8, 1]))
    b = np.array([0.5, 1, 0])
    x = crout(A, b)
    print("X:\n", x)

if __name__=="__main__":
    main()
