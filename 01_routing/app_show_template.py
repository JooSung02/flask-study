from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '🏠 Home Page'

@app.route('/hello/<name>')
def greet(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True) 