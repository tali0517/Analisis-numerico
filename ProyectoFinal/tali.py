from flask import Blueprint, render_template, request ,  abort

history =[]

tali = Blueprint('tali', __name__,
                        template_folder='templates',
                        static_folder='static')

@tali.route('/')
def show():
    return render_template("index.html")

@tali.route('form' , methods=["POST", "GET"])
def form():
    fx = request.form.get('fx')
    grid= request.form.get('grid')
    history.append(f"{fx} {grid}")
    title= "graph"
    return render_template("form.html", title=title, history= history, fx=fx)


