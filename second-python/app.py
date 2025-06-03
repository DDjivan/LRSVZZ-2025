from flask import Flask, render_template
from os import path

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
        html_data = markdown(md_data, extras=['tables', 'footnotes', 'fenced-code-blocks', 'break-on-newline'])
    else:
        html_data = markdown(md_data, extensions=['tables', 'footnotes', 'fenced_code', 'breaks'])

    return html_data

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app = Flask(__name__)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from re import sub, MULTILINE

def convert_https_links(text):
    pattern = r'(?<!\]\()' + r'https://[^\s]+'

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

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

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

    with open(sPath, 'r', encoding='utf-8') as file:
        md_data = file.read()

    md_data = convert_https_links(md_data)
    md_data = convert_strikethrough_text(md_data)

    html_data = md_to_html(md_data)

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
