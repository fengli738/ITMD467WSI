from flask import Flask
#coding:utf8

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"

if __name__ == '__main__':
    app.run()