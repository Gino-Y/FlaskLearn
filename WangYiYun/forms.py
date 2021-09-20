from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10,
                                              message='用户名长度必须在3到10位之间')])
    password = StringField(validators=[Length(min=3, max=10,
                                              message='用户名长度必须在3到10位之间')])
    password_repeat = StringField(validators=[Length(min=3, max=10,
                                                     message='两次密码输入不一致'), EqualTo('password')])


class LoginForm(Form):
    email = StringField(validators=[Email()])
