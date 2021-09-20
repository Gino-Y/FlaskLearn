from flask import Flask, request, render_template
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10,
                                              message='用户名长度必须在3到10位之间')])
    password = StringField(validators=[Length(min=3, max=10,
                                              message='用户名长度必须在3到10位之间')])
    password_repeat = StringField(validators=[Length(min=3, max=10,
                                              message='两次密码输入不一致'), EqualTo('password')])


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'get':
        return render_template(r'WangYiYun/templates/regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True)