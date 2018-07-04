@app.route('/',methods=['get','post'])
def index():
    if request. method=='POST'
        start=request.form['start']
        end=request.form['end']
        total=countDaysDiffer(start,end)

    return render_template('index.html',countsDays=total,hidden='')
else:
    return render_template('index.html', hidden='hidden')
