from flask import Blueprint

from flask import render_template



app_dev = Blueprint('dev', __name__)



@app_dev.route('/dev')
def web_dev() :
    return render_template('dev.html')
