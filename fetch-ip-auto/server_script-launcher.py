from flask import Flask, render_template
from subprocess import run
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_script')
def execute_script():
    # '-p' = execute the command on RPi4 via SSH
    # run(['ssh', '-p', '50000', 'user@localhost', 'bash /path/to/your_script.sh'])
    run(['ssh', '-p', '50001', 'nous@localhost', 'echo "Current date: $(date)" > ~/TEST.txt'])

    current_time = datetime.now().isoformat().replace('T', ' ')

    return "Script executed! " + current_time

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)
