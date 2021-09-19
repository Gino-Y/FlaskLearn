from flask import Flask, request
import config
import talib

print(talib.__file__)
exit()
# 创建一个flask对象
app = Flask(__name__)
app.config.from_object(config)
app.config.from_pyfile('config.tex', silent=True)


@app.route('/')  # 装饰器
def hello_world():
    return 'Hello World!'


@app.route('/list/')
def article_list():
    return 'article list'


# 多路径
@app.route('/article/test/')
def article_test():
    return 'article test'


# 参数
@app.route('/article/<article_id>/')
def article_detail(article_id):
    return '您请求的文章是: %s' % article_id


# 参数指定数据类型
@app.route('/p/<int:article_id>/')
def article_type(article_id):
    return '您请求的文章是: %s' % article_id


# 多路径path
@app.route('/article/<path:test>/')
def article_path(test):
    return 'article path'


# uuid
@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心页面: %s' % user_id


# import uuid
# print(uuid.uuid4())


# blog
# user
# 多个路径映射
@app.route('/<any(blog, user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情：%s' % id
    else:
        return '用户详情：%s' % id
# http://127.0.0.1:5000/user/1/
# http://127.0.0.1:5000/blog/1/


# ? 不需要SEO优化：搜索引擎检索到
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    return '您通过查询字符串的方式传递的参数是：%s' % wd
# http://127.0.0.1:5000/d/?wd=python/


if __name__ == '__main__':
    # 启动一个测试应用服务器
    app.run()
