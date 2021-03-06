# coding=utf-8
from flask import Flask, render_template, request

from countdays import countDaysDiffer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        total = countDaysDiffer(start, end)
        return render_template('index.html', countDays=total, hidden='')
    else:
        return render_template('index.html', hidden='hidden')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)  # accept external post
    # 10.222.248.184