from flask import Flask, request
from datetime import datetime



sFile = 'rpi4_ip.txt'



app = Flask(__name__)

@app.route('/update_ip', methods=['POST'])
def update_ip() :
    hostname   = request.form['hostname']
    username   = request.form['username']
    ip_address = request.form['ip']

    current_time = datetime.now().isoformat().replace('T', ' ')  # ISO 8601 but remove the T

    # write datetime, IP address, hostname, and username in a file
    with open(sFile, 'a') as f :
        f.write(f'{current_time} - {ip_address} - {hostname} - {username}\n')

    return 'RPi2-Listener here. Well received the three of your data!', 200

@app.route('/view_ips', methods=['GET'])
def view_ips() :
    try :
        with open(sFile, 'r') as f :
            content = f.read()

        return f'<pre>{content}</pre>'  # return content in a preformatted text block

    except FileNotFoundError :
        return 'The file is empy: no IP addresses recorded yet.', 404



if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=50000)
