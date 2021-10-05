#!/home/salzatec1/miniconda3/bin/python

from sympy import *
import math

def secante(func, x0, x1, Nmax, tol):
    x = Symbol('x')
    f = lambdify(x, func)
    fDer1 = lambdify(x, func.diff(x))

    f0 = f(x0)
    f1 = f(x1)
    E = 1000
    i = 1

    while i < Nmax and E > tol:
        xact = x1 -f1*((x1-x0)/(f1-f0))
        fact = f(xact)
        print("X{i} =".format(i=i), xact,"|","f(x{i}) =".format(i=i), fact,"|","Error =", E)
        E = abs(xact-x1)
        x0 = x1
        f0 = f1
        x1 = xact
        f1 = fact
        i += 1

    if i == Nmax or E > tol:
        print("El metodo no converge con los datos dados")
    else:
        print("X{i} =".format(i=i), xact,"|","f(x{i}) =".format(i=i), fact,"|","Error =", E)
        print("El metodo converge a x:", xact, "en la iteracion", i)

def main():
    x = Symbol('x')
    secante(funcion(x), 0.5, 1, 100, 1e-7)

def funcion(x):
    #return math.exp(x) + math.sin(x)
    return ln(sin(x)**2 +1) - 1/2

if __name__=='__main__':
    main()
