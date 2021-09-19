from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/hello

@app.route('/hello',methods=["GET"])  # HttpRequest
@app.route('/hello2',methods=["GET"])  # HttpRequest
def hello_world():
    return "Hello World!" #,"500 ERROR"

# print(__name__)
if __name__ == '__main__': # 表示当前文件是程序入口 
    app.run() # 5000