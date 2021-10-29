#!/home/salzatec1/miniconda3/bin/python
import numpy as np
from gausstot import gausstot

def vandermonde(X, Y):
    n = X.size
    A = np.zeros((n, n)) # (shape)
    X = np.matrix.transpose(X)

    for i in range(n):
        A[:,i] = np.matrix.transpose(np.power(X, (n-i-1)))
        print(n-i)

    coef = gausstot(A, np.matrix.transpose(Y))
    return coef

def main():
    X = np.array([1, 2, 3, 4, 5])
    
    Y = np.array([1, 2, 3, 4, 5])
    coef = vandermonde(X, Y)

    print("Coef:\n", coef)

if __name__=="__main__":
    main()
