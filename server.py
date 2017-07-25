from flask import Flask, render_template, request, jsonify, g
from flask_cors import CORS, cross_origin
import sqlite3
app = Flask(__name__)
CORS(app)

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

@app.route('/list.json')
def weblog():
    list = [
        {
            'componentType': 'text',
            'content': "Sup, yo."
        },
        {
            'componentType': 'snippet',
            'content': "I drink and I know things."
        }
    ]
    return jsonify(results=list)

# http://localhost:5000/query?file=foo.html
@app.route('/query')
def query():
    if 'file' in request.args:
        query_filename = request.args.get('file')
        return render_template(query_filename)
    else:
        return 'nothing specified'

@app.route('/data', methods=['POST'])
def data():
    data = jsonify(request.json)
    component_type = request.get_json()['post']['component_type']
    content = request.get_json()['post']['content']
    post = (component_type,) + (content,)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?)", post)
    conn.commit()
    conn.close()
    read_data()
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_debugger=False)
