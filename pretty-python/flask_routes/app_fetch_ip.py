from flask import Blueprint

from flask import request, render_template
from flask_routes.md_util import *
from datetime import datetime



app_ip = Blueprint('ip', __name__)



FILE_DATA = '../fetch-ip/rpi4_ip.txt'



@app_ip.route('/update_ip', methods=['POST'])
def update_ip() :
    hostname   = request.form['hostname']
    username   = request.form['username']
    ip_address = request.form['ip']

    current_time = datetime.now().isoformat().replace('T', ' ')  # ISO 8601 but remove the T

    # write datetime, IP address, hostname, and username in a file
    with open(FILE_DATA, 'a') as f :
        f.write(f'{current_time} - {ip_address} - {hostname} - {username}\n')

    return 'RPi2-Listener here. Well received the three of your data!', 200



@app_ip.route('/view_ips', methods=['GET'])
def view_ips() :
    try :
        with open(FILE_DATA, 'r') as f :
            content = f.read()

        # return f'<pre>{content}</pre>'
        content = f'<pre>{content}</pre>'

    except FileNotFoundError :
        # return 'The file is empy: no IP addresses recorded yet.', 404
        content = "The file is empy: no IP addresses recorded yet."

    finally:
        new_content = md_to_html(content)
        return render_template('dev.html', content=new_content)


