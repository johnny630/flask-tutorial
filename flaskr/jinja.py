from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('jinja', __name__, url_prefix='/jinja')

@bp.route('/tutor')
def tutor():
    data = {
        'name': 'johnny',
        'mylist': ['johnny', 'rachel']
    }
    return render_template('jinja/tutor.html', data=data)