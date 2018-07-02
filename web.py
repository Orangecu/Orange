# coding=utf-8
from flask import Flask, redirect

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
     return '吃醋的橘子!'
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080,debug=True)
