from flask import Blueprint, render_template, abort

urrego = Blueprint('urrego', __name__,
                        template_folder='templates',
                        static_folder='static')

@urrego.route('/methods/vandermonde/<string:array>', methods=['GET','POST'])
def vandermonde_route(array):
    data = {}
    data['title'] = 'Vandermonde'
    print(array)
    return render_template('interpolation/vandermonde.html', data = data)

@urrego.route('/methods/newton/<string:array>', methods=['GET','POST'])
def newton_interpolation_route(array):
    data = {}
    data['title'] = 'Newton'
    return render_template('interpolation/newton.html', data = data)

@urrego.route('/methods/lagrange/<int:array>', methods=['GET','POST'])
def lagrange_route(array):
    data = {}
    data['title'] = 'Lagrange'
    data['array_len'] = array
    return render_template('interpolation/lagrange.html', data = data)

@urrego.route('/methods/spline_linear/<string:array>', methods=['GET','POST'])
def spline_linear_route(array):
    data = {}
    data['title'] = 'Spline Linear'
    return render_template('interpolation/spline_linear.html', data = data)

@urrego.route('/methods/spline_square/<string:array>', methods=['GET','POST'])
def spline_square_route(array):
    data = {}
    data['title'] = 'Spline Square'
    return render_template('interpolation/spline_square.html', data = data)

@urrego.route('/methods/spline_cubica/<string:array>', methods=['GET','POST'])
def spline_cubic_route(array):
    data = {}
    data['title'] = 'Spline Cubic'
    return render_template('interpolation/spline_cubic.html', data = data)
