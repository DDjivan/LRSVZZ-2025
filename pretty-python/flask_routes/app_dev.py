from flask import Blueprint

from flask import render_template
from subprocess import run
from datetime import datetime



app_dev = Blueprint('dev', __name__)



@app_dev.route('/dev')
def web_dev() :
    return render_template('dev.html')

@app_dev.route('/dev/send', methods=['POST'])
def send_plans() :

    port = 50001
    remote_host = "nous@localhost"
    # directory = '~/PLANS_A_RESOUDRE'
    directory = '/home/dd/PLANS_A_RESOUDRE'
    current_time = datetime.now().isoformat().replace('T', ' ')

    # scp -P port path/to/local_file remote_host:path/to/remote_file
    # scp -r remote_host:path/to/remote_directory path/to/local_directory
    # scp -P 50001 -r ~/PLANS_A_RESOUDRE nous@localhost:~

    try:
        run(
            ["scp", "-P", str(port), "-r", directory, f'{remote_host}:~'],
            check=True
        )
        return f"[{current_time}] Sent! \n" #+' '.join(["scp", "-P", str(port), "-r", f'{remote_host}:{directory}', directory])
        # print(' '.join(["scp", "-P", str(port), "-r", f'{remote_host}:{directory}', directory]))

    except Exception as e:
        return f"[{current_time}] Python Error: \n{str(e)}", 500


