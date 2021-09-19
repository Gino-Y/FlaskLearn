from flask import Flask, render_template
import config

app = Flask(__name__)


@app.route('/')  # 装饰器
def hello_world():
    context = {
        'username': 'ziliao',
        'age': 18,
        'country': 'China',
        'childrens': {
            'name': 'Gino',
            'height': 180
        }
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    # 启动一个测试应用服务器
    app.run()
