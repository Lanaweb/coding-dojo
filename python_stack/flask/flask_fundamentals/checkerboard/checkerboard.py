from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def originalcheck():
    return render_template('check.html')
    
@app.route('/row')
def checkboard():
    return render_template('check.html')
    
@app.route('/play/<int:time>')
def style1(time):
    return render_template('style1.html', block =time)


@app.route('/play/<int:time>/<color>')
def style2(time, color):
    return render_template('style2.html', block =time, back=color)

@app.route('/repeat/<int:timess>/<string>')
def repeat_string_times(timess, string):
    return string * times

if __name__=="__main__":
    app.run(debug=True)