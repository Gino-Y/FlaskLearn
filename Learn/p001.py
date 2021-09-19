from flask import Flask, request

app = Flask(__name__)


@app.route('/t1/<p1>/<p2>')
def m001(p1, p2):
    return p1 + "/" + p2


@app.route('/t2/<int:p1>/')
def m002(p1):
    return str( type(p1) )

@app.route('/t3/<path:p1>/')
def m003(p1):
    return p1

"""
# 参数指定数据类型
@app.route('/p/<int:article_id>/')
def article_type(article_id):
    return '您请求的文章是: %s' % article_id
#   /p/整数


# 多路径path
@app.route('/article/<path:test>/')
def article_path(test):
    return 'article path'

# uuid
@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心页面: %s' % user_id

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
"""

if __name__ == '__main__':
    # 启动一个测试应用服务器
    app.run()