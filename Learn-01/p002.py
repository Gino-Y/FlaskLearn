# 路径参数
# https://blog.csdn.net/qq_39147299/article/details/109366209

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义类型转换器
class MobileConverter(BaseConverter):
    regex = "1[3-9]\d{9}$"  # 匹配规则，不要以^开头


app.url_map.converters["mobile"] = MobileConverter  # 添加到转换器列表


@app.route(rule="/user/<mobile:mobile>")  # 将参数uid转换成mobile类型
def index(mobile):
    print(type(mobile))
    return str(mobile)


# 1.定义类，继承自BaseConverter
class MyRegexConverter(BaseConverter):
    # 2.重写init方法,接收两个参数
    def __init__(self, map, regex):
        # 3.初始化父类成员变量，还有子类自己的规则
        super(MyRegexConverter, self).__init__(map)
        self.regex = regex


# 4.将转换器类，添加到系统默认的转换器列表中
app.url_map.converters['wdc'] = MyRegexConverter


# 三位整数
@app.route('/<wdc("\d{3}"):num>')
def hello_world(num):
    return f'这一个数是{num}'


class ListConverter(BaseConverter):

    def to_python(self, values):
        """
        将url中的参数转换为我们需要的数据类型
        """
        # split方法就是去掉加号并返回list类型数据
        tmp = values.split('+')
        return tmp

    def to_url(self, values):
        """
        将[1,2,3]转换成1+2+3
        """
        # 遍历列表values中的数据，以+连接，最后tmp1的值即1+2+3
        # tmp1 = '+'.join([BaseConverter.to_url(self, value) for value in values])
        tmp1 = '+'.join(values)
        return tmp1


# 将写好的类注册到DEFAULT_CONVERTERS
app.url_map.converters['list'] = ListConverter


@app.route('/detail/<list:params>/')
def detail(params):
    print('params:%s' % params)
    return 'success for url'


if __name__ == '__main__':
    app.run(debug=True)
