#!/home/salzatec1/miniconda3/bin/python

import math

def reglafalsa(func, a, b, Nmax, tol):
    if a > b:
        print("'A' cannot be greather than 'B'")
        return

    fa = func(a)
    fb = func(b)
    pm = (fb*a-fa*b)/(fb-fa)
    fpm = func(pm)
    
    E = 1000
    count = 1
    print("|{i:^3}|{a:^20}|{xm:^20}|{b:^20}|{fxm:^20}|{E:^10}|".format(i="i",a="a",xm="xm",b="b",fxm="f(xm)",E="E"))
    while (count < Nmax) and (E > tol):
        print("|{i:3g}| {a:.16f} | {xm:.16f} | {b:.16f} | {fpm:.16f} | {E:.1E} |".format(i=count, a=a, xm=pm, b=b, fpm=fpm, E=E))
        #print(count, " - (a =",a,"b =",b,")")
        if (fa * fpm) < 0:
            b = pm
            fb = fpm
        else:
            a = pm
            fa = fpm
        
        p0 = pm
        pm = (fb*a - fa*b)/(fb-fa)
        fpm = func(pm)
        E = abs(pm-p0)
        count += 1

    if count == Nmax or E > tol:
        print("El metodo no esta convergiendo")
    else:
        print("|{i:3g}| {a:.16f} | {xm:.16f} | {b:.16f} | {fpm:.16f} | {E:.1E} |".format(i=count, a=a, xm=pm, b=b, fpm=fpm, E=E))

def funcion(x):
    #return math.exp(x) + math.sin(x)
    return math.log(math.sin(x)**2 + 1) - 1/2

def main():
    reglafalsa(funcion, 0, 1, 100, 1e-7)

if __name__ == '__main__':
    main()
