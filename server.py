from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import sqlite3
app = Flask(__name__)
CORS(app)

# conn = sqlite3.connect('weblog.db')
# print "Opened database successfully";
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print "Table created successfully";
# conn.close()

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

@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    print user

if __name__ == '__main__':
    app.run(debug=True, port=5000)
