#!/home/salzatec1/miniconda3/bin/python

import math

def biseccion(func, a, b, Nmax, tol):
    if a > b:
        print("'A' cannot be greather than 'B'")
        return

    fa = func(a)
    fb = func(b)
    pm = a + (b-a)/2
    fpm = func(pm)
    
    E = 1000
    count = 1
    while (count < Nmax) and (E > tol):
        print(count, " - (a =",a,", b =",b,")")
        if (fa * fpm) < 0:
            b = pm
            fb = fpm
        else:
            a = pm
            fa = fpm
        p0 = pm
        pm = (a+b)/2
        fpm = func(pm)
        E = abs(p0-pm)

        count += 1

def funcion(x):
    #return math.exp(x) + math.sin(x)
    return math.log(math.sin(x)**2 + 1) - 1/2

def main():
    biseccion(funcion, 0, 1, 100, 1e-7)


if __name__ == '__main__':
    main()
