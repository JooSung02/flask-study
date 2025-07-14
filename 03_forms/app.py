from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>👋 Hello! Go to <a href="/greet">/greet</a> to try the form.</p>'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return f'<h2>Hello, {name}!</h2>'
    return render_template('greet.html')

if __name__ == '__main__':
    app.run(port=5003)
