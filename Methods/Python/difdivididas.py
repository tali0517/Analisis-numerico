#!/home/salzatec1/miniconda3/bin/python
import numpy as np

def difdivididas(X, Y):
    n = X.size
    D = np.zeros((n, n)) # (shape)
    X = np.matrix.transpose(X)

    D[:,0] = np.matrix.transpose(Y)
    for i in range(1, n):
        aux0 = D[i-1:n, i-1]
        aux = np.diff(aux0)
        aux2 = X[i:n] - X[0:n-i]
        D[i:n, i] = np.divide(aux, aux2)

    coef = np.diag(D)
    return coef

def main():
    X = np.array([1, 2, 3, 4, 5, 6, 7])
    
    Y = np.array([3, 54, 2, -2, 0.2, -1, 0])
    coef = difdivididas(X, Y)
    print(coef)

if __name__=="__main__":
    main()
