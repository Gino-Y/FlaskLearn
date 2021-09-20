
from flask import Flask,request,make_response,session,redirect
app = Flask(__name__)

app.config["SECRET_KEY"]="123"

#  A系统 把token值发给登陆校验系统进行校验
#  B系统
#  C系统
#  登陆校验系统 登陆页面  发token accessToken refreshToken -> 浏览器  每次请求 A B C 携带token
#
# 1. 访问业务系统时 如果没有accessToken就调整到 登陆校验系统中  登陆 登陆后，重新向到具体业务系统
# 浏览器发出: http://ip/service1Sys/aaa
# service1Sys 发现里面没有accessToken 返回信息{无权限请登陆}
# 浏览器发出：http://ip2/loginSys/login?redirectUrl=http://ip/service1Sys/aaa
# loginSys -> login.html
# 登陆请求，如果通过，就重定向到redirectUrl对应的页面
#
# 2. 访问业务系统时，如果有accessToken
# 业务系统 把收到accessToken 远程调用 登陆校验系统 进行校验
# 如果校验不通过，把校验不通过的信息返回给浏览器
# 浏览器会把 refreshToken 发给 登陆校验系统 得到新的 accessToken refreshToken
# 浏览用新的 accessToken 访问业务系统
#

@app.route("/login",methods=["GET","POST"])
def login():
    resp = make_response("LOGIN SUCCESS")
    session["username"] = request.args.get("username")
    return resp

@app.route("/main",methods=["GET","POST"])
def amin():
    if "username" not in session:
        #return redirect("http://127.0.0.1:5000/login.html")
        return '{"code":3}'
    else:
        return "WELCOME,"+session["username"]


@app.route("/getCookie/aaa/bbb/ccc",methods=["GET","POST"])
def getToken():
    resp = make_response("SUCCESS")
    resp.set_cookie("sessionId","001",path="/getInfo/")
    resp.set_cookie("cookie004","bbbb",max_age=10)
    return resp

@app.route("/getInfo/aaa/b",methods=["GET"])
def getInfo():
    return request.cookies.get("cookie005")


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