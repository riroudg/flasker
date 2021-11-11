from flask import Flask, render_template

### Create a flask instance
app1 = Flask(__name__)

### Create a route decorator
@app1.route('/')


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

@app1.route('/user/<name>')

def user22(name):
  return render_template('user.html', name=name)

### Create Custom Error Pages

###   Invalid URL
@app1.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

###  Internal Server Error
@app1.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

