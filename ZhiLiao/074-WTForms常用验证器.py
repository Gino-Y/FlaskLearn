from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'get':
        pass
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)