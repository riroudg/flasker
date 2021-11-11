from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

### Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my super secret key'

### Create a Form Class
class NamerForm(FlaskForm):
  name = StringField("What's you Name", validators=[DataRequired()])
  submit = SubmitField("Submit you name")



### Create a route decorator
@app.route('/')


### jinja filters:
# save     bedeutet: html code wird ausgefuehrt
#
# capitalize	bedeutet: den ersten Buchstaben gross schreiben
# lower		bedeutet: alles klein schreiben
# upper		bedeutet: alles gross schreiben
# title		bedeutet: jeden ersten Buchstaben in einem word gross schreiben
# trim		bedeutet: Leerzeichen am Ende entfernen
# striptags	bedeutet: html code wird entfernt
# 		der default ist: html code wird als text angezeigt

def index():

  stuff = 'This is <strong>bold</strong> Text';
  favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
  return render_template('index.html', 
    favorite_pizza=favorite_pizza,
    stuff=stuff)

@app.route('/user/<name>')

def user22(name):
  return render_template('user.html', name=name)

### Create Custom Error Pages

###   Invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

###  Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

### Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
  name = None
  form = NamerForm()

  ### Validate the data from the Form
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
    flash("the form submit was successfull")

  return render_template('name.html',
	name = name,
	form = form)

