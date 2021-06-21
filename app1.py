from flask import Flask

app = Flask(__name__)

@app.route('/a')
def hello_world():
    return 'Hello world'