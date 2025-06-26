from flask import Blueprint

from flask import render_template

app_canvas = Blueprint('draw', __name__)

@app_canvas.route('/draw', methods=['GET'])
def canvas_page():
    return render_template('canvas_page.html')
