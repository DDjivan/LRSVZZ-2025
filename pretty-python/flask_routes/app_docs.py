from flask import Blueprint

from flask import Flask, render_template
from flask_routes.md_util import *



app_docs = Blueprint('docs', __name__)



@app_docs.route('/docs')
def web_doc() :
    sREADME = path.join('../', 'README.md')

    with open(sREADME, 'r', encoding='utf-8') as file:
        md_data = file.read()

    # html_data = markdown(md_data)
    html_data = markdown(md_data, extras={
        'breaks': {'on_newline': True, 'on_backslash': True},
        'tables': True,
        'footnotes': True
    })

    return render_template('doc.html', content=html_data)

@app_docs.route('/<path:filename>')
def web_markdown(filename:str) :

    sPath = path.join('../', filename)
    text_file_extensions = ['.py', '.sh', '.html', '.css', '.js', '.json', '.txt', ]

    if not path.isfile(sPath):
        return render_template('index.html', content=render_error('404 Not Found'))

    if not filename.endswith('.md'):
        if not any(filename.endswith(ext) for ext in text_file_extensions):
            return send_file(sPath)  # utile pour les images et les pdf

    try:
        with open(sPath, 'r', encoding='utf-8') as file:
            data = file.read()
    except Exception as e:
        return render_template('index.html', content=render_error(e))

    for extension in text_file_extensions:
        if filename.endswith(extension):
            return render_template('index.html', content=f'<pre>{data}</pre>')

    data = convert_https_links(data)
    data = convert_strikethrough_text(data)
    data = convert_highlighted_text(data)

    html_data = md_to_html(data)

    return render_template('index.html', content=html_data)
