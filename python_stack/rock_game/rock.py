from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
    
@app.route('/result', methods = ["POST"])
def player_pick():
	gamedic = {
	 'rock' : {"scissor": "win", "rock":'tie', 'paper':'lose'},
	 'scissor' : {"scissor": "tie", "rock":'lose', 'paper':'win'},
	 'paper' : {"scissor": "lose", "rock":'win', 'paper':'tie'}
	}
	choices = ['rock','paper','scissor']
	player_two= random.choice(choices)
	print (gamedic[request.form['player_selection']][player_two])
	print('In player')
	print('Request.form', request.form)
	print('Player Selects', request.form['player_selection'])
	return render_template('index.html', player_one = request.form['player_selection'], player_two = player_two, result =gamedic[request.form['player_selection']][player_two] )
    

if __name__=="__main__":
    app.run(debug=True)