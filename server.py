from flask import Flask, render_template, request, jsonify, g
from flask_cors import CORS, cross_origin

import flask
import flask_cors
import sqlite3
app = flask.Flask(__name__)
flask_cors.CORS(app)

def read_data():
    print 'inside read_data() function'
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE component_type='test'")
    selected_data = c.fetchall()
    print selected_data

@app.route('/')
def display():
    print "WELCOME TO THE FOLD."
    return render_template('index.html')

@app.route('/post')
def weblog():
    post = {
            "date": "kjsdck",
            "title": ",m ,ms",
            "elements": [
                {
                  "type": "text",
                  "content": "Sup, yo."
                },
                {
                  "type": "snippet",
                  "content": "Hello, I am content"
                },
                {
                  "type": "snippet",
                  "content": "and yup"
                },
                {
                  "type": "snippet",
                  "content": "It was a good day!"
                }
            ]
        }
    return jsonify(post=post)

# http://localhost:5000/query?file=foo.html
@app.route('/query')
def query():
    if 'file' in flask.request.args:
        query_filename = flask.request.args.get('file')
        return flask.render_template(query_filename)
    else:
        return 'nothing specified'

@app.route('/data', methods=['POST'])
def data():
    component_type = flask.request.get_json()['post']['component_type']
    content = flask.request.get_json()['post']['content']
    post = (component_type,) + (content,)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?)", post)
    conn.commit()
    conn.close()
    read_data()
    return flask.jsonify({})

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_debugger=False)
