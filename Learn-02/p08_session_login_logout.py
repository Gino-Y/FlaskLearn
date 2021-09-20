from flask import Flask,request,make_response,session,redirect,jsonify
app = Flask(__name__)

#pip install flask-cors
from flask_cors import *  # 导入模块
CORS(app, supports_credentials=True)  # 设置跨域

app.config["SECRET_KEY"]="123"
users = {
    "zhangsan":"1234",
    "lisi":"1234"
}

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username] == password:
        session["username"] = username
        return '{"code":0,"msg":"success"}', \
               200, {"content-type": "application/json"}
    else:
        return '{"code":1,"msg":"用户名或密码错误"}'

@app.route("/logout",methods=["GET"])
def logout():
    session["username"] = None
    return '{"code":0,"msg":"success"}', \
           200, {"content-type": "application/json"}

def isLogin():
    return "username" in session and session["username"] is not None

@app.route("/getLoginUser",methods=["GET"])
def getLoginUser():
    if not isLogin():
        return '{"code":3,"msg":"未登陆"}'
    r = {"code":0,"msg":"success","data":session["username"]}
    print(jsonify(**r))
    return jsonify(**r) # jsonify(code=0,msg="success",..)


if __name__ == '__main__':
    app.run(debug=True)
