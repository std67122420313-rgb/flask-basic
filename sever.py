from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return f'<h1>Hello word!</h1>'

@app.route('/name')
def name():
   return f'<h1>siwakon</h1>'

##if __name__ == '__main__':
   ##app.run(debug=True)
