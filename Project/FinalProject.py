from flask import Flask, request, render_template, make_response, redirect, url_for, flash

from flask import Flask, render_template
from flask_wtf import Form 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class LoginForm(Form):
	username = StringField('username', validators=[InputRequired()])
	password = PasswordField('password', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def Cookie():
	printed = make_response('<h1 style="color:blue;padding-left: 500px;">  <h1> Welcome To The Soccer Fanpage  </h1> <br> <a href = "/Login" > LoginPage</a> </br>    <br> <a href = "/players" > Players</a>   </br>  <br> <a href = "/GOAT" > Who is the Best Player in the world?</a>   </br>     ')
	printed.set_cookie('Leo', 'Messi')
	return printed


@app.route('/Login', methods=['GET', 'POST'])
def Login():
	form = LoginForm()
	if form.validate_on_submit():
		return render_template('indexzz.html')
	return render_template('index.html', form=form)

@app.route('/players', methods=['GET', 'POST'])
def Players():
	symbols = {"Messi":"Lionel Messi", "Ronaldo": "Cristiano Ronaldo", "Neymar": "Neymar Santos", "Pique": "Gerrard Pique"}
	return render_template('ListOfPlayer.html', symbols=symbols)

@app.route('/GOAT')
def insert_image():
	return render_template ("image.html")




@app.route ('/player/<Name>')
def ursign(Name):
        
	playerlist = ["Messi","Ronaldo","Neymar","Pique"]
	if Name in playerlist:
		return render_template("viewer.html", Name = Name)
	else:
		return "Invalid Link . Choose Only from HyperLinks "





@app.errorhandler(404)
def Error(e):
	return render_template("Error1.html")

@app.errorhandler(405)
def Error1(e):
	return render_template("Error1.html")



if __name__ == '__main__':
	app.run(debug=True)
