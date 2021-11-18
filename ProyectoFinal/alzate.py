from flask import Blueprint, render_template, abort, request
from io import StringIO
import sys
import numpy as np
from Methods.Python.gausspl import gausspl
from Methods.Python.gausspar import gausspar
from Methods.Python.gausstot import gausstot
from Methods.Python.lusimpl import lusimpl
from Methods.Python.lupar import lupar
from Methods.Python.crout import crout
from Methods.Python.doolittle import doolittle
from Methods.Python.cholesky import cholesky
from Methods.Python.jacobi import jacobi
from Methods.Python.gseidel import gseidel
from Methods.Python.sor import sor

alzate = Blueprint('alzate', __name__,
                        template_folder='templates',
                        static_folder='static')

@alzate.route('/')
def show():
    return render_template('Linear/gausspl.html')

@alzate.route('/methods/gausspl', methods=['GET', 'POST'])
def gausspl_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausspl(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausspl.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/gausspar', methods=['GET', 'POST'])
def gausspar_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausspar(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausspar.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/gausstot', methods=['GET', 'POST'])
def gausstot_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausstot(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausstot.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/lusimpl', methods=['GET', 'POST'])
def lusimpl_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = lusimpl(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/lusimpl.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/lupar', methods=['GET', 'POST'])
def lupar_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = lupar(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/lupar.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/crout', methods=['GET', 'POST'])
def crout_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = crout(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/crout.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/doolittle', methods=['GET', 'POST'])
def doolittle_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = doolittle(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/doolittle.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/cholesky', methods=['GET', 'POST'])
def cholesky_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    if request.method == 'POST':
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
                b[i] =  float(request.form["fieldb"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = cholesky(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/cholesky.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/jacobi', methods=['GET', 'POST'])
def jacobi_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    x0 = np.zeros(3)
    tol = 0
    nmax = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(3):
            x0[i] = float(request.form["fieldx"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = jacobi(A, b, x0, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/jacobi.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/gseidel', methods=['GET', 'POST'])
def gseidel_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    x0 = np.zeros(3)
    tol = 0
    nmax = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(3):
            x0[i] = float(request.form["fieldx"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gseidel(A, b, x0, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gseidel.html', st = st, x = x, stdout = result_stdout)

@alzate.route('/methods/sor', methods=['GET', 'POST'])
def sor_route():
    A = np.zeros((3,3))
    b = np.zeros(3)
    x0 = np.zeros(3)
    tol = 0
    nmax = 0
    w = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        w = float(request.form["fieldw"])
        for i in range(3):
            for j in range(3):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(3):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(3):
            x0[i] = float(request.form["fieldx"+str(i)])

    st = matrix_str(A)
    st = st.split('\n')
    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = sor(A, b, x0, w, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/sor.html', st = st, x = x, stdout = result_stdout)

def matrix_str(A):
    mstr = ''
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            mstr += "{number: .3f}".format(number = A[i][j])
        mstr += '\n'

    return mstr
