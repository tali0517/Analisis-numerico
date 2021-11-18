from flask import Blueprint, render_template, abort, request
from io import StringIO
import sys
from Methods.Python.gausspl import gausspl
from Methods.Python.gausspar import gausspar
from Methods.Python.gausstot import gausstot
from Methods.Python.lusimpl import lusimpl
from Methods.Python.lupar import lupar
import numpy as np

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

def matrix_str(A):
    mstr = ''
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            mstr += "{number: .3f}".format(number = A[i][j])
        mstr += '\n'

    return mstr
