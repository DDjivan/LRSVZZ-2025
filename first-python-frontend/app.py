from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/bdd_rpi.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.getcwd(), "instance", "bdd_rpi.db")}'
print("Current working directory:", os.getcwd())  # DEBUG
print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])  # DEBUG

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RaspberryPi(db.Model):
    __tablename__ = 'raspberry_pis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    delivery_step = db.Column(db.String(100), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/raspberrypis', methods=['GET'])
def get_raspberry_pis():
    raspberry_pis = RaspberryPi.query.all()
    print(raspberry_pis)  # DEBUG
    return jsonify([{
        'id': pi.id,
        'name': pi.name,
        'status': pi.status,
        'delivery_step': pi.delivery_step,
        'last_updated': pi.last_updated
    } for pi in raspberry_pis])


@app.route('/api/raspberrypis', methods=['POST'])
def add_raspberry_pi():
    data = request.json
    new_pi = RaspberryPi(
        name=data['name'],
        status=data['status'],
        delivery_step=data['delivery_step']
    )
    db.session.add(new_pi)
    db.session.commit()
    return jsonify({'id': new_pi.id}), 201



@app.route('/main')
def main():
    raspberry_pis = RaspberryPi.query.all()
    return render_template('main.html', raspberry_pis=raspberry_pis)



if __name__ == '__main__':
    # db.create_all()
    with app.app_context():  # Create an application context
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
