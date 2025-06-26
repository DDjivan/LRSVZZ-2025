from flask import Blueprint

from flask import render_template



app_home = Blueprint('home', __name__)



@app_home.route('/')
def web_home() :
    return render_template('index.html')

@app_home.route('/choix')
def web_choix() :
    return render_template('choix.html')
