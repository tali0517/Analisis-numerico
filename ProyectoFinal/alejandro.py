from flask import Blueprint, render_template, abort, request
from io import StringIO
import sys
import math
from sympy import sympify, evalf, symbols

from Methods.Python.busquedaIncremental import busqueda
from Methods.Python.biseccion import biseccion
from Methods.Python.reglafalsa import reglafalsa
from Methods.Python.puntofijo import puntofijo
from Methods.Python.newton import newton
from Methods.Python.secante import secante
from Methods.Python.raicesmlt import raicesmlt

alejandro = Blueprint('alejandro', __name__,
                        template_folder='templates',
                        static_folder='static')

@alejandro.route('/')
def show():
    return render_template('singleVariable/incSearch.html')


@alejandro.route('/methods/incsearch', methods=['GET', 'POST'])
def incsearch_route():

    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        function = request.form['function']
        xin = float(request.form['xin'])
        delta = float(request.form['delta'])
        nmax = int(request.form['nmax'])

        funct = sympify(function)

        stdout = StringIO()
        sys.stdout = stdout
        x = busqueda(funcion, xin, delta, nmax)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/incSearch.html', x=x, stdout=result_stdout)

    return render_template('singleVariable/incSearch.html')


@alejandro.route('/methods/bisection', methods=['GET', 'POST'])
def bisection_route():

    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        function = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        nmax = int(request.form['nmax'])
        tol = int(request.form['tol'])

        funct = sympify(function)

        stdout = StringIO()
        sys.stdout = stdout
        x = biseccion(funcion, a, b, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/bisection.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/bisection.html')

@alejandro.route('/methods/falsepos', methods=['GET', 'POST'])
def falsepos_route():
    def function(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2
    a = 0
    b = 0.5
    nmax = 100
    tol = math.exp(-7)

    if request.method == 'POST':
        function = request.form['function']
        a = request.form['a']
        b = request.form['b']
        nmax = request.form['nmax']
        tol = request.form['tol']

    stdout = StringIO()
    sys.stdout = stdout
    x = reglafalsa(function, a, b, nmax, tol)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('singleVariable/falsepos.html', x=x, stdout = result_stdout)


@alejandro.route('/methods/fixedpoint', methods=['GET', 'POST'])
def fixedpoint_route():
    def function(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2 - x

    def functiong(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2
    x0 = 0
    nmax = 100
    tol = math.exp(-7)

    if request.method == 'POST':
        f = request.form['function']
        g = request.form['fung']
        xini = request.form['xini']
        nmax = request.form['nmax']
        tol = request.form['tol']

    stdout = StringIO()
    sys.stdout = stdout
    x = puntofijo(function, g, xini, nmax, tol)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('singleVariable/fixedpoint.html', x=x, stdout = result_stdout)


@alejandro.route('/methods/newtonraphs', methods=['GET', 'POST'])
def newtonraphs_route():
    def function(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2 - x
    x0 = 0
    nmax = 100
    tol = math.exp(-7)

    if request.method == 'POST':
        f = request.form['function']
        fdx = request.form['fdx']
        xini = request.form['xini']
        nmax = request.form['nmax']
        tol = request.form['tol']

    stdout = StringIO()
    sys.stdout = stdout
    x = newton(f, fdx, xini, nmax, tol)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('singleVariable/newtonraphs.html', x=x, stdout = result_stdout)


@alejandro.route('/methods/secant', methods=['GET', 'POST'])
def secant_route():
    def function(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2 - x
    x0 = 0
    nmax = 100
    tol = math.exp(-7)

    if request.method == 'POST':
        f = request.form['function']
        x0 = request.form['xin']
        x1 = request.form['x']
        nmax = request.form['nmax']
        tol = request.form['tol']

    stdout = StringIO()
    sys.stdout = stdout
    x = secante(f, x0, x1, nmax, tol)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('singleVariable/newtonraphs.html', x=x, stdout = result_stdout)

@alejandro.route('/methods/multiroots', methods=['GET', 'POST'])
def multiroots_route():
    def function(x):
        return math.log(math.sin(x) ** 2 + 1) - 1 / 2 - x
    x0 = 0
    nmax = 100
    tol = math.exp(-7)

    if request.method == 'POST':
        f = request.form['function']
        fdx = request.form['fdx']
        f2dx = request.form['f2dx']
        x0 = request.form['xin']
        nmax = request.form['nmax']
        tol = request.form['tol']

    stdout = StringIO()
    sys.stdout = stdout
    x = raicesmlt(f, fdx, f2dx,x0, nmax, tol)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('singleVariable/multipleroots.html', x=x, stdout = result_stdout)

