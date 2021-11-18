from flask import Blueprint, render_template, abort

urrego = Blueprint('urrego', __name__,
                        template_folder='templates',
                        static_folder='static')

@urrego.route('/methods/vandermonde')
def vandermonde_route():
    data = {}
    data['title'] = 'Vandermonde'
    return render_template('interpolation/vandermonde.html', data = data)

@urrego.route('/methods/newton')
def newton_interpolation_route():
    data = {}
    data['title'] = 'Newton'
    return render_template('interpolation/newton.html', data = data)

@urrego.route('/methods/lagrange')
def lagrange_route():
    data = {}
    data['title'] = 'Lagrange'
    return render_template('interpolation/lagrange.html', data = data)

@urrego.route('/methods/spline_linear')
def spline_linear_route():
    data = {}
    data['title'] = 'Spline Linear'
    return render_template('interpolation/spline_linear.html', data = data)

@urrego.route('/methods/spline_square')
def spline_square_route():
    data = {}
    data['title'] = 'Spline Square'
    return render_template('interpolation/spline_square.html', data = data)

@urrego.route('/spline_cubica')
def spline_cubic_route():
    data = {}
    data['title'] = 'Spline Cubic'
    return render_template('interpolation/spline_cubic.html', data = data)
