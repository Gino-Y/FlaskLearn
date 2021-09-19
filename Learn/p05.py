"""
method url 协议版本
请求头

请求体

GET url xxx
xxx
xxx

默认没有请求体

POST url xxx
xxx
xxx

一般把数据放在请求体中 数据可以是任意格式

method：GET POST PUT DEL ..
url: 携带参数
   /xx/xxx/x1xx/xxx  后端从路径中获取其中一部分 路径参数 x1xx  route(/<xx>)
   /xx/xxx?a=2&a=3&xcv=  查询参数  url参数   request.args.getlist

在请求的header中应该包含 请求体的信息（格式）
content-type:text  application/json  xt
form-data    a=2&a=3&x=4
application/json  {"xx":xx}
text  asdf
html  <html> ... </html>
xml  <xml>..
 request.form


return "json格式的字符串",200,{"content-type":"application/json"}

停车场后端系统 停车场工作人员 和 高德地图

数据放在内存

"""

from flask import Flask, request
import tokenUtil

app = Flask(__name__)

# {"parkId":"1","status":"空闲"}
#
parkDict = {
    "1": "空闲",
    "2": "空闲",
    "3": "空闲"
}
# {"username":"张三","password":"xxx"}
userDict = {
    "zs": "123456",
    "ls": "123456"
}


# {"token":"xxxx","refreshToken":"用来作废旧token换新token的凭证"}
@app.route("/getToken", methods=["POST"])
def getToken():
    username = request.json.get("username")
    password = request.json.get("password")
    token = tokenUtil.genToken(username)
    if (userDict[username] == password):
        return '{"code":0,"msg":"success","token":"' + token + '"}', \
               200, {"content-type": "application/json"}
    else:
        return '{"code":1,"msg":"用户名或密码错误"}'


@app.route("/setInfo", methods=["POST"])
def setInfo():
    token = request.json.get("token")
    # 验证token是否正确
    if not tokenUtil.validateToken(token):
        return '{"code":1,"msg":"token is invalid"}', 200, {"content-type": "application/json"}

    parkId = request.json.get("parkId")
    parkStaus = request.json.get("status")
    parkDict[parkId] = parkStaus
    print(parkDict)
    return '{"code":0,"msg":"success"}', 200, {"content-type": "application/json"}


# /getInfo?id=?
# {"status":"空闲"}
@app.route("/getInfo", methods=["GET"])
def getInfo():
    print(parkDict)
    parkId = request.args.get("id")
    parkStaus = parkDict[parkId]
    return '{"status":"' + parkStaus + '"}', 200, {"content-type": "application/json"}


# 1. 路径参数
# 2. url?xxx=xx&xx=xxx  request.args
# 3. xxx=xxxx&xxxx=xxx在请求body中  "multipart/form-data"   request.form
# 4. {"xx":xx}  "application/json"  request.json


if __name__ == '__main__':
    app.run(debug=True)

# 联系高德
# 1.标注一个停车场
# 2.签协议
# 3.
