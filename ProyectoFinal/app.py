from flask import Flask, render_template
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
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
