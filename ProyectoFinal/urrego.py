from flask import Blueprint, render_template, abort

urrego = Blueprint('urrego', __name__,
                        template_folder='templates',
                        static_folder='static')

@urrego.route('/methods/vandermonde/<int:array>', methods=['GET','POST'])
def vandermonde_route(array):
    data = {}
    data['title'] = 'Vandermonde'
    
    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/vandermonde.html', data = data)

@urrego.route('/methods/newton/<int:array>', methods=['GET','POST'])
def newton_interpolation_route(array):
    data = {}
    data['title'] = 'Newton'

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array

    return render_template('interpolation/newton.html', data = data)

@urrego.route('/methods/lagrange/<int:array>', methods=['GET','POST'])
def lagrange_route(array):
    data = {}
    data['title'] = 'Lagrange'
    
    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/lagrange.html', data = data)

@urrego.route('/methods/spline_linear/<int:array>', methods=['GET','POST'])
def spline_linear_route(array):
    data = {}
    data['title'] = 'Spline Linear'
    
    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_linear.html', data = data)

@urrego.route('/methods/spline_square/<int:array>', methods=['GET','POST'])
def spline_square_route(array):
    data = {}
    data['title'] = 'Spline Square'
    
    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_square.html', data = data)

@urrego.route('/methods/spline_cubica/<int:array>', methods=['GET','POST'])
def spline_cubic_route(array):
    data = {}
    data['title'] = 'Spline Cubic'
    
    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_cubic.html', data = data)
