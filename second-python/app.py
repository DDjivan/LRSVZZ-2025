from flask import Flask, render_template
from markdown2 import markdown
# from markdown import markdown
from os import path

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app = Flask(__name__)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

@app.route('/')
def home() :
    sREADME = path.join('../', 'README.md')

    with open(sREADME, 'r', encoding='utf-8') as file:
        md_data = file.read()

    # html_data = markdown(md_data)
    html_data = markdown(md_data, extras={
        'breaks': {'on_newline': True, 'on_backslash': True},
        'tables': True,
        'footnotes': True
    })

    return render_template('index.html', content=html_data)

@app.route('/<path:filename>')
def serve_markdown(filename:str) :

    sPath = path.join('../', filename)

    with open(sPath, 'r', encoding='utf-8') as file:
        md_data = file.read()

    # html_data = markdown(md_data, extras={
    #     'breaks': {'on_newline': True, 'on_backslash': True},
    #     'tables': True,
    #     'footnotes': True,
    #     'fenced-code-blocks': True
    # })
    html_data = markdown(md_data, extras=[
        'break-on-newline',
        'tables',
        'footnotes',
        'fenced-code-blocks'
    ])

    # return render_template_string(html_data)
    return render_template('index.html', content=html_data)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from subprocess import run
from datetime import datetime
# from json import load

@app.route('/execute_script')
def execute_script():

    sCommand = 'echo "JS to Python to Bash: $(date +%Y-%m-%dT%H:%M:%S.%6N)" > ~/TEST.txt'
    lRun = [sCommand]

    run(lRun, shell=True)

    current_time = datetime.now().isoformat().replace('T', ' ')

    return "JS to Python to HTML: " + current_time

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=50000, debug=True)
