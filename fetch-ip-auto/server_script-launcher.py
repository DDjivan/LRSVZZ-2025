from flask import Flask, render_template
from subprocess import run
from datetime import datetime
from json import load



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_script')
def execute_script():

    with open('./tunnel/client_tunnelconfig.json') as file:
        config = load(file)

    nPort = config['PORT']
    sUsername = "nous"
    sCommand = 'echo "Client over SSH: $(date +%Y-%m-%dT%H:%M:%S.%6N)" > ~/TEST.txt'


    sRun = f"ssh -p {nPort} {sUsername}@localhost"
    lRun = sRun.split(' ') + [sCommand]

    run(lRun)

    current_time = datetime.now().isoformat().replace('T', ' ')

    return "Server local output: " + current_time



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
