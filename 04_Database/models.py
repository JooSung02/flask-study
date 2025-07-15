from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # SQLAlchemy라는 DB 툴을 연결

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 각 메모의 고유번호
    content = db.Column(db.String(200), nullable=False)  # 메모 내용, 필수입력

    def __repr__(self):
        return f'<Memo {self.content}>'