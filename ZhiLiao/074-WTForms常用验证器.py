from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET'])
def regist():
    if regist.method == 'get':
        pass
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)