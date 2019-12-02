from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Main Page'
    
@app.route('/list')
def render_list():
	students_name = [
		{'first_name': "Michael", 'last_name': 'Choi'},
		{'first_name': "John", 'last_name': 'Susupin'},
		{'first_name': "Mark", 'last_name': 'Guillen'}
	]
	return render_template('index.html', students = students_name)
    

if __name__=="__main__":
    app.run(debug=True)