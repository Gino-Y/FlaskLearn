from flask import Flask, request, make_response
import tokenUtil

app = Flask(__name__)

# {"parkId":"1","status":"空闲"}
#
parkDict = {
    "1": "空闲",
    "2": "空闲",
    "3": "空闲"
}
userDict = {
    "zs": "123456",
    "ls": "123456"
}

# session

sessionStore = {"001": session1}


@app.route("/login", methods=["GET", "POST"])
def login():
    resp = make_response("LOGIN SUCCESS")
    resp.set_cookie("sessionId", "001", path="/")
    session["001"] = {}
    session["001"]["username"] = request.args.get("username")
    return resp


@app.route("/main", methods=["GET", "POST"])
def amin():
    if "sessionId" not in request.cookies:
        return "NOT LOGIN"
    else:
        sessionId = request.cookies.get("sessionId")
        return "WELCOME," + session[sessionId]["username"]


@app.route("/getCookie/aaa/bbb/ccc", methods=["GET", "POST"])
def getToken():
    resp = make_response("SUCCESS")
    resp.set_cookie("sessionId", "001", path="/getInfo/")
    resp.set_cookie("cookie004", "bbbb", max_age=10)
    return resp


@app.route("/getInfo/aaa/b", methods=["GET"])
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
