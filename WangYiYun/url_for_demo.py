from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return url_for('my_list', page=1)
    # return 'sdgsdgsd'


@app.route('/list/<page>')
def my_list(page):
    return 'my list'


if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')
