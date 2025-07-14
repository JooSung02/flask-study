from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>🚪 Welcome! Go to <a href="/login">Login</a></p>'   # home을 설정 안해주면 들어갔을 때 404 나옴

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        return f'<h2>Welcome, {user}!</h2><p>Your password is {pw}</p>'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=5001)  # 5000은 다른 데에서 쓰고 있으니까 다르게 설정