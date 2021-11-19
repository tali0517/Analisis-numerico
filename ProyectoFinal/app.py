from flask import Flask, render_template
import sys
#sys.path.append('/home/salzatec1/Analisis-numerico/ProyectoFinal/Methods/Python')
sys.path.append('Methods/Python')

from alzate import alzate
from alejandro import alejandro
from urrego import urrego
from tali import tali


app = Flask(__name__)
app.register_blueprint(alzate, url_prefix='/alzate')
app.register_blueprint(alejandro, url_prefix='/alejandro')
app.register_blueprint(urrego, url_prefix='/urrego')
app.register_blueprint(tali, url_prefix='/tali')


@app.route('/')
def hello():
    return render_template("nav/index.html")

@app.route('/methods')
def methods_route():
    return render_template("nav/methods.html")

@app.route('/aboutUs')
def about_us_route():
    return render_template("nav/about_us.html")

@app.route('/help')
def help_route():
    return render_template("nav/help.html")

if __name__ == "__main__":
    app.run(debug=True)
