from flask import Flask, render_template
from subprocess import run
from datetime import datetime
from configparser import ConfigParser



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_script')
def execute_script():
    # nPort = 50001
    config = ConfigParser()
    config.read('./tunnel/client_tunnelconfig.cfg')
    nPort = config.get('DEFAULT', 'PORT')
    sUsername = "nous"
    sCommand = "echo 'Current date: $(date)' > ~/TEST.txt"

    sRun = f"ssh -p {nPort} {sUsername}@localhost"
    lRun = sRun.split(' ') + [sCommand]

    run(lRun)

    current_time = datetime.now().isoformat().replace('T', ' ')

    return "Script executed! " + current_time



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)
