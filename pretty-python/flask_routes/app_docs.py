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

    if not path.isfile(sPath):
        return render_template('doc.html', content=f'<h1>404 Not Found</h1>')

    with open(sPath, 'r', encoding='utf-8') as file:
        data = file.read()

    if not filename.endswith('.md'):
        return render_template('doc.html', content=f'<pre>{data}</pre>')

    data = convert_https_links(data)
    data = convert_strikethrough_text(data)
    data = convert_highlighted_text(data)

    html_data = md_to_html(data)

    # return render_template_string(html_data)
    return render_template('doc.html', content=html_data)

