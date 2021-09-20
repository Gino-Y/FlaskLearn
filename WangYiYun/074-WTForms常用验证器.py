from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'get':
        return render_template(r'WangYiYun/templates/regist.html')
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)