from flask import Blueprint, render_template, abort

tali = Blueprint('tali', __name__,
                        template_folder='templates',
                        static_folder='static')

@tali.route('/')
def show():
    return render_template("Methods.html")
