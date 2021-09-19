from flask import Flask, request, redirect, url_for
import config

app = Flask(__name__)


@app.route('/')  # 装饰器
def hello_world():
    return 'Hello World!'


@app.route('/login/')  # 装饰器
def login():
    return '这是登录页面'


@app.route('/profile/')  # 装饰器
def profile():
    if request.args.get('name'):
        return '个人中心页面'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    # 启动一个测试应用服务器
    app.run()
