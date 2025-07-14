from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home() :
    return '<h2>Welcome! Go to <a href="/login">/login</a> to start</h2>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '1234':
            return redirect(url_for('info'))
        else:
            error = '❌ 잘못된 사용자명 또는 비밀번호입니다.'
    return render_template('login.html', error=error)

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        return render_template('info.html', name=name, email=email, age=age)
    return render_template('info.html', name=None)

memos = []

@app.route('/memo', methods=['GET', 'POST'])
def memo():
    global memos
    if request.method == 'POST':
        note = request.form['note']
        if note:
            memos.append(note)
    return render_template('memo.html', memos=memos)

if __name__ == '__main__':
    app.run(port=5005)