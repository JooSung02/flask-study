# 04 - DataBase (SQLAlchemy)

Flask에서 SQLAlchemy를 활용한 데이터베이스 연동을 학습한 실습입니다.
메모를 추가, 조회, 삭제하고 전체 삭제하는 기능까지 구현했습니다.


## 학습 내용

- SQLAlchemy 설치 및 설정
- DB 모델 정의 및 초기화
- 메모 추가 (Create)
- 메모 조회 (Read)
- 메모 삭제 (Delete)
- 전체 삭제 기능
- 삭제 전에 DB 비어있는지 체크


## 📝 주요 기능

### 1. 메모 추가 (Create)
- 사용자가 입력한 메모를 데이터베이스에 저장
- 빈 입력은 저장되지 않도록 처리

### 2. 메모 조회 (Read)
- 저장된 모든 메모를 리스트로 출력
- 메모가 없을 경우 “아직 메모가 없습니다” 출력

### 3. 메모 삭제 (Delete)
- 각 메모 옆에 ❌ 삭제 버튼 제공
- 삭제 버튼 클릭 시 해당 메모만 삭제

### 4. 전체 삭제
- 전체 삭제 버튼을 누르면 모든 메모 삭제
- 데이터가 없으면 삭제되지 않음

---

## 🧪 코드 스니펫

### 모델 정의

```python
class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)