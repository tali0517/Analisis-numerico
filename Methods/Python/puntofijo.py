#!/home/salzatec1/miniconda3/bin/python

import math

def puntofijo(g, x0, Nmax, tol):
    print(" i |  X")
    print("----------------")
    xant = x0
    E = 1000
    count = 0
    while (count < Nmax) and (E > tol):
        print("{0:02d}".format(count), "|", xant)
        xact = g(xant)
        E = abs(xact-xant)
        xant = xact
        count += 1

    x = xact
    err = E

def funcion(x):
    return math.log((math.sin(x)**2) + 1) - 1/2

def main():
    puntofijo(funcion, -0.5, 100, 1e-7)


if __name__ == '__main__':
    main()
