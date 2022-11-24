from flask import Flask
import os

app = Flask(__name__)

@app.route('/<name>')
def hello(name=None):
    if(name):
        return "Hello " + str(name)
    else
        return "Hello World!"



if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
