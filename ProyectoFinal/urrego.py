from flask import Blueprint, render_template, abort

urrego = Blueprint('urrego', __name__,
                        template_folder='templates',
                        static_folder='static')

@urrego.route('/')
def show():
    return "hOLA Urrego"
