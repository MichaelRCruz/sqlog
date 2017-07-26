import flask
import flask_cors
import sqlite3
app = flask.Flask(__name__)
flask_cors.CORS(app)

# conn = sqlite3.connect('database.db')
# c = conn.cursor()
#
# c.execute('CREATE TABLE elements (element_id INTEGER PRIMARY KEY, element_type TEXT NOT NULL, content TEXT NOT NULL, post_id INTEGER NOT NULL, FOREIGN KEY (post_id) REFERENCES posts(post_id))')
#
# c.execute('CREATE TABLE posts (post_id INTEGER PRIMARY KEY, post_date TEXT, title TEXT, subtitle TEXT)')

# conn.commit()
# conn.close()

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
            "post_date": "date",
            "title": "title",
            "subtitle": "subtitle",
            "elements": [
                {
                  "element_type": "text",
                  "content": "Sup, yo."
                },
                {
                  "element_type": "snippet",
                  "content": "Hello, I am content"
                },
                {
                  "element_type": "snippet",
                  "content": "and yup"
                },
                {
                  "element_type": "snippet",
                  "content": "It was a good day!"
                }
            ]
        }
    return flask.jsonify(post=post)

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
    date = flask.request.get_json(force=False)['post']['post_date']
    print date
    # title = flask.request.get_json()['post']['title']
    # subtitle = flask.request.get_json()['post']['subtitle']
    # elements = flask.request.get_json()['post']['elements']
    # post = (date, title, elements)
    # conn = sqlite3.connect('database.db')
    # c = conn.cursor()
    # c.execute("INSERT INTO posts VALUES (?, ?, ?)", post)
    # conn.commit()
    # conn.close()
    # read_data()
    return flask.jsonify({})

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_debugger=False)
