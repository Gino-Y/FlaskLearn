from flask import Flask, request
app = Flask(__name__)

@app.route("/p1",methods=["GET","POST"])
def m003():
    print(request.args["password"])
    print(request.args.get("password",None))
    print(request.args.getlist("password",None))
    print(request.form) # body中的 xxx = xxx
    print(request.json)
    return str(request.args)

# 1. 路径参数
# 2. url?xxx=xx&xx=xxx  request.args
# 3. xxx=xxxx&xxxx=xxx在请求body中  "multipart/form-data"   request.form
# 4. {"xx":xx}  "application/json"  request.json


if __name__ == '__main__':
    app.run(debug=True)