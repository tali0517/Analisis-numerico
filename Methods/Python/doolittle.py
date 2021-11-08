#!/home/salzatec1/miniconda3/bin/python

from sustreg import sustreg
from sustprog import sustprog
import numpy as np

def doolittle(A, b):
    n = np.array(A.shape[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(0, n):
        for j in range(i, n):
            U[i][j] = A[j][i] - L[i, 0:i-1].dot(np.matrix.transpose(U[0:i-1,i]))

        for j in range(i+1, n):
            L[j][i] = np.divide((A[j][i] - L[j, 0:i-1].dot( np.matrix.transpose(U[0:i-1,i]))), U[i][i])

    U[n-1][n-1] = A[n-1][n-1] - L[n-1, 0:n-2].dot(np.matrix.transpose(U[0:n-2,n-1]))

    z= sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))

def main():
    A = np.array(([1,2],
                 [1,2]))
    b = np.array([1, 2])

    doolittle(A, b)


if __name__=="__main__":
    main()
