from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/list/', methods=['GET', 'POST'])
def my_list():
    return 'list'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'

if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')
