from flask import Blueprint, render_template, abort

alejandro = Blueprint('alejandro', __name__,
                        template_folder='templates',
                        static_folder='static')

@alejandro.route('/')
def show():
    return "HOLA Alejandro"
