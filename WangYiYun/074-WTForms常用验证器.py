from flask import Flask, request, render_template
from forms import RegistForm


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


@app.route('/Login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)