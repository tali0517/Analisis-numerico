#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg

def gseidel(A, b, x0, tol, Nmax):
    det = np.linalg.det(A) # Determinant of matrix
    if det == 0:
        print("Determinant of matrix is 0")
        return
    D = np.diag(np.diag(A))
    L = -np.tril(A)+D
    U = -np.triu(A)+D
    
    T = np.linalg.inv(D-L).dot(U)
    C = np.linalg.inv(D-L).dot(b)
    xant = x0
    E = 1000
    cont = 0

    while E>tol and cont<Nmax:
        np.set_printoptions(precision=8, suppress=True)
        print("{i:2d} | X{i} = {xant} | E = {Err:.1E}".format(i=cont, xant=xant, Err=E))
        xact = T.dot(xant+C)
        E = np.linalg.norm(xant-xact)
        xant = xact
        cont += 1

    if E>tol or cont == Nmax:
        print("This method can not get solution to the matrix")
    else:
        print("{i} | X{i} = {xant} | E = {Err:.1E}".format(i=cont, xant=xant, Err=E))

def main():
    #size = 4
    #A = np.random.rand(size, size)
    #b = np.random.rand(size)
    #A = np.array(([2, -1, 0, 3], 
    #             [1, 0.5, 3, 8], 
    #             [0, 13, -2, 11], 
    #             [14, 5, -2, 3]))
    #b = np.array([1, 1, 1, 1])
    A = np.random.rand(3,3)
    #A = np.array(([0, 0, 1],
    #            [4, 2, 1],
    #            [0.81, 0.9, 1]))
    b = np.array([0.5, 1, 0])
    x0 = np.array([0, 0, 0])
    gseidel(A, b, x0, 1e-7, 100)


if __name__ == '__main__':
    main()
