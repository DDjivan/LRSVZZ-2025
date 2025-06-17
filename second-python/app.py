from flask import Flask, render_template

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

try:
    from markdown2 import markdown
    MARKDOWN_LIBRARY = 'markdown2'
except ImportError:
    try:
        from markdown import markdown
        MARKDOWN_LIBRARY = 'markdown'
    except ImportError:
        raise ImportError("No Markdown library available. Please install either markdown or markdown2.")

def md_to_html(md_data) :
    if MARKDOWN_LIBRARY == 'markdown2':
        html_data = markdown(md_data, extras=['tables', 'footnotes', 'fenced-code-blocks', 'break-on-newline', 'mdx_math'])
    else:
        html_data = markdown(md_data, extensions=['tables', 'footnotes', 'fenced_code', 'breaks', 'mdx_math'])

    return html_data

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app = Flask(__name__)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from re import sub, MULTILINE

def convert_https_links(text):
    pattern = r'(?<!\]\()' + r'http(s)?://[^\s]+'

    # text_with_links = sub(pattern, r'[\1](\1)', text, flags=MULTILINE)

    def escape_underscores(match):
        url = match.group(0)
        escaped_url = url.replace('_', r'\_')
        return f'[{escaped_url}]({escaped_url})'

    text_with_links = sub(pattern, escape_underscores, text, flags=MULTILINE)

    return text_with_links

def convert_strikethrough_text(text):
    pattern = r'~~(.*?)~~'
    result = sub(pattern, r'<s>\1</s>', text)
    return result

def convert_highlighted_text(text):
    pattern = r'==(.*?)=='
    result = sub(pattern, r'<mark>\1</mark>', text)
    return result

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from os import path

@app.route('/')
def web_home() :
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
def web_markdown(filename:str) :

    sPath = path.join('../', filename)

    if not path.isfile(sPath):
        return render_template('index.html', content=f'<h1>404 Not Found</h1>')

    with open(sPath, 'r', encoding='utf-8') as file:
        data = file.read()

    if not filename.endswith('.md'):
        return render_template('index.html', content=f'<pre>{data}</pre>')

    data = convert_https_links(data)
    data = convert_strikethrough_text(data)
    data = convert_highlighted_text(data)

    html_data = md_to_html(data)

    # return render_template_string(html_data)
    return render_template('index.html', content=html_data)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from flask import request
from datetime import datetime

sFile = '../fetch-ip/rpi4_ip.txt'

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

        # return f'<pre>{content}</pre>'  
        content = f'<pre>{content}</pre>'

    except FileNotFoundError :
        # return 'The file is empy: no IP addresses recorded yet.', 404
        content = "The file is empy: no IP addresses recorded yet."

    finally: 
        new_content = md_to_html(content)
        return render_template('index.html', content=new_content)

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
