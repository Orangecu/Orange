# coding=utf-8
from flask import Flask, redirect

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
     return "<a href='/new'>点击这里哦!&nbsp;&nbsp;&nbsp; </a><a href='/old'>这里也可以点!&nbsp;&nbsp;&nbsp;</a><br><a href='/o1'>别点上面点这里!&nbsp;&nbsp;&nbsp;</a><a href='/o2'>别理他们点我!&nbsp;&nbsp;&nbsp;</a>"
@app.route('/new',methods=['GET','POST'])

def new():
     return "<a href='/'>为什么你让你点，你就点了那</a>"

@app.route('/old',methods=['GET','POST'])
def old():
    return "<a href='/'>你好哦</a>"

@app.route('/o1',methods=['GET','POST'])
def o1():
    return "<a href='/'>yooooo</a>"

@app.route('/o2',methods=['GET','POST'])
def o2():
    return "<a href='/'>halahala</a>"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080,debug=True)

