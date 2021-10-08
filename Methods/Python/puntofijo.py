#!/home/salzatec1/miniconda3/bin/python

import math

def puntofijo(f, g, x0, Nmax, tol):
    print(" i |  X")
    print("----------------")
    xant = x0
    gant = g(xant)
    fant = f(xant)
    E = 1000
    count = 0
    print("|{i:^3}|{xi:^20}|{gxi:^20}|{fxi:^20}|{E:^10}|".format(i="i",xi="xm",gxi="g(xi)",fxi="f(xi)",E="E"))
    while (count < Nmax) and (E > tol):
        print("|{i:3g}| {xi:.16f} | {gxi:.16f} | {fxi:.16f} | {E:.1E} |".format(i=count, xi=xant, gxi=gant, fxi=fant, E=E))
        #print("{0:02d}".format(count), "|", xant)
        xact = gant
        E = abs(xact-xant)
        xant = xact
        gant = g(xant)
        fant = f(xant)
        count += 1

    if count == Nmax or E > tol:
        print("El metodo no converge ocn los datos dado")
    else:
        print("|{i:3g}| {xi:.16f} | {gxi:.16f} | {fxi:.16f} | {E:.1E} |".format(i=count, xi=xant, gxi=gant, fxi=fant, E=E))
        #print("|{i:3g}| {xi:.16f} | {gxi:.16f} | {E:.1E} |".format(i=count, xi=xant, gxi=gant, E=E))
        
    x = xact
    err = E

def funciong(x):
    return math.log((math.sin(x)**2) + 1) - 1/2

def funcion(x):
    return math.log((math.sin(x)**2) + 1) - 1/2 -x

def main():
    puntofijo(funcion, funciong, -0.5, 100, 1e-7)


if __name__ == '__main__':
    main()
