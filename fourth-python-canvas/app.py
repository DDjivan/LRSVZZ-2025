from flask import Flask

from flask_routes.app_canvas_draw import app_canvas
from flask_routes.app_canvas_upload import app_upload

app = Flask(__name__)

app.register_blueprint(app_canvas)
app.register_blueprint(app_upload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
