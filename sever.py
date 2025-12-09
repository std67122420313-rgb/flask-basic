from flask import Flask
import uuid
app = Flask(__name__)

@app.route('/')
def index():
  return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask Basic</title>
</head>
<body>
  <h1>Home page</h1>
  <hr>
</body>
</html>
"""

@app.route('/name')
def name():
   return f'<h1>siwakon</h1>'

@app.route('/user/<username>')
def user(username):
   return f'<h1>My name is {username}</h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a, b):
   return f'<h1>{a} + {b} = {a+b}</h1>'

@app.route('/calculator/Subtraction/<int:a>/<int:b>')
def addition(a, b):
   return f'<h1>{a} - {b} = {a-b}</h1>'

@app.route('/calculator/Multiplication/<int:a>/<int:b>')
def addition(a, b):
   return f'<h1>{a} * {b} = {a*b}</h1>'

@app.route('/calculator/Division/<int:a>/<int:b>')
def addition(a, b):
   return f'<h1>{a} / {b} = {a/b}</h1>'
   
@app.route('/secretkey/<uuid:sk>')
def my_secret_key(sk):
   return f'<h1> My secret Key: {sk}<h1>'

##if __name__ == '__main__':
   ##app.run(debug=True)
