from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/')
def hello_world():
    return 'Hello HBNB!'

@app.route('/hbnb')
def HBNB():
    return 'HBNB'

@app.route('/c/<text>')
def TEXT(text):
    text = str(text).replace("_", " ")
    return 'C {}'.format(escape(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
