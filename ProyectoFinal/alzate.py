from flask import Blueprint, render_template, abort

alzate = Blueprint('alzate', __name__,
                        template_folder='templates',
                        static_folder='static')

@alzate.route('/')
def show():
    return "hOLa Alzarres"
