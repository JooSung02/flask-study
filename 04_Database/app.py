from flask import Flask, render_template, request, redirect, url_for
from models import db, Memo

app = Flask(__name__)  # 지금 이 파일에서 Flask를 시작
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memos.db'  # 어떤 DB를 사용할지. 여기서는 SQLite라는 DB를 memos.db라는 파일로 만들겠다.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 변경사항 추적 끄기 (불필요함)

db.init_app(app)  # Flask 앱 객체와 models.py의 db = SQLAlchemy를 연결

@app.route('/', methods=['GET', 'POST'])  # GET - 처음 웹페이지 열 때 (읽기) , POST - 폼을 제출할 때 (쓰기)
def memo():  # 사용할 함수
    if request.method == 'POST':  # 저장 버튼을 누른 경우
        content = request.form['note']  # HTML에서 보낸 데이터를 딕셔너리 형태로 받음
        if content:  # 제대로 내용을 제출했으면
            new_memo = Memo(content=content)  # models.py에서 만든 클래스로 새로운 객체 생성, 작성한 내용을 content에 저장
            db.session.add(new_memo)  # 방금 만든 메모를 데이터베이스 세션에 등록, 저장은 아니고 준비만
            db.session.commit()  # DB에 진짜 저장
        return redirect(url_for('memo'))  # 현재 라우트를 다시 호출해서 새로고침
    memos = Memo.query.all()  # DB에 저장된 모든 메모를 가져옴 , Memo 테이블에 저장된 모든 메모를 memo 리스트에 담아두기
    return render_template('memo.html', memos=memos) # memos라는 데이터를 html에 넘겨서 html 화면 출력

@app.route('/delete/<int:memo_id>', methods=['POST'])  # 삭제 기능 (특정 memo의 id를 받아 삭제하는 방식) 이 경로로 POST가 오면 memo_id를 인자로 받아 삭제 처리
def delete_memo(memo_id):  # 연결된 삭제 함수
    memo_to_delete = Memo.query.get(memo_id)  # DB에서 해당 ID를 가진 메모를 가져옴  Memo.query.get은 기본 키를 기준으로 데이터를 가져오는 메서드
    if memo_to_delete:  # 해당 id에 메모가 있으면 (= 삭제할 내용이 있으면)
        db.session.delete(memo_to_delete)  # DB 세션에 이 메모를 삭제할 거라고 지정해둠
        db.session.commit()  # 예약해둔 메모를 실제로 DB에서 삭제
    return redirect(url_for('memo'))  # 다시 기본 화면으로 초기화 (memo() 함수와 연결된 라우트로 이동)

@app.route('/delete_all/', methods=['POST'])
def delete_all() :
    if Memo.query.count() > 0 :
        Memo.query.delete()
        db.session.commit()
    return redirect(url_for('memo'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5006, debug=True)


