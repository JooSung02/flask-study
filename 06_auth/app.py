from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 세션을 위한 키

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# 앱 실행 전 DB 테이블 생성
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return '<h2>Welcome! Go to <a href="/register">Register</a> or <a href="/login">Login</a></h2>'

@app.route('/register', methods=['GET', 'POST'])
def register() :
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user :
            error = '이미 존재하는 사용자 입니다.'
            return render_template('register.html', error = error)
        
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))  # 로그인 성공 시 이동할 페이지
        else:
            error = '❌ 사용자 이름 또는 비밀번호가 잘못되었습니다.'
    
    return render_template('login.html', error=error)

@app.route('/find', methods=['GET', 'POST'])
def find():
    result = None
    error = None

    if request.method == 'POST':
        action = request.form['action']

        if action == 'find_pw':
            username = request.form['find_pw_username']
            user = User.query.filter_by(username=username).first()
            if user:
                result = f"🔐 비밀번호는 👉 {user.password}"
            else:
                error = "해당 사용자 이름이 존재하지 않습니다."

        elif action == 'find_user':
            input_pw = request.form['find_user_password']
            users = User.query.all()
            found = False
            for user in users:
                if check_password_hash(user.password, input_pw):
                    result = f"🧑 해당 비밀번호를 가진 사용자: {user.username}"
                    found = True
                    break
            if not found:
                error = "일치하는 비밀번호를 가진 사용자가 없습니다."

    return render_template('find.html', result=result, error=error)

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            message = f"✅ 사용자 '{username}' 계정이 삭제되었습니다."
        else:
            message = "❌ 해당 사용자를 찾을 수 없습니다."

    return render_template('delete_user.html', message=message)


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f"<h2>🎉 로그인 성공! 사용자 ID: {session['user_id']}</h2>"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5007, debug=True)

