# Flask-SQLAlchemy

[Flask-SQLAlchemy 공식문서](http://flask-sqlalchemy.pocoo.org/2.1/)

## 연동 설정

* ```SQLALCHEMY_DATABASE_URI```
    * ```sqlite:////absolute/path/to/foo.db```
    * ```mysql://scott:tiger@localhost/mydatabase```
    * ```oracle://scott:tiger@127.0.0.1:1521/sidname```
    * ```postgresql://scott:tiger@localhost/mydatabase```
* ```SQLALCHEMY_TRACK_MODIFICATIONS```
    * 2.1 버전부터는 명시적으로 False로 지정할 것
    
## 모델 정의

### User 모델 정의 예시

* ```id```: 정수
* ```username```: 문자열, VARCHAR(80)
* ```email```: 문자열, VARCHAR(120)

* db 생성

```python
>>> from hello import db
>>> db.create_all()
```

* User 생성 (메모리)

```python
>>> from hello import User
>>> admin = User('admin', 'admin@example.com')
>>> guest = User('guest', 'guest@example.com')
```

* User 삽입 (DB 테이블)

```python
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()
```

* User 질의, 검색

```python
>>> users = User.query.all()
[<User u'admin'>, <User u'guest'>]
>>> admin = User.query.filter_by(username='admin').first()
<User u'admin'>
```

### 모델/뷰 파일 모듈로 분리 및 설정 클래스

* ```config``` 모듈 ```Configuration``` 클래스에 SQLAlchemy 관련 설정 멤버 변수 선언
* ```run.py```에 models를 임포트
* ```models.py``` 파일을 새로 만들어 필요한 모델 정의
* ```__init__.py```에 SQLAlchemy db 객체 선언
* ```from run import db``` 임포트로 ```db.create_all()``` 호출
    * ```db.create_all()``` 호출하기 전에 반드시 모델이 먼저 임포트되어 있어야 한다.

## 관계 정의

## CRUD

### 레코드 삽입

1. 파이썬 객체 생성
1. Flask-SQLAlchemy 세션에 추가
1. Flask-SQLAlchemy 세션을 커밋

```python
>>> from yourapp import User
>>> me = User('admin', 'admin@example.com')
>>> db.session.add(me)
>>> me.id
>>> db.session.commit()
>>> me.id
1
```

* 커밋 전에는 me.id값이 없고 커밋해야 비로소 ID값을 구할 수 있다.

### 레코드 삭제

```python
>>> db.session.delete(me)
>>> db.session.commit()
```

### 레코드 질의

| id | username | email |
|----|----------|-------|
| 1 | admin | admin@example.com |
| 2 | peter | peter@example.org |
| 3 | guest | guest@example.com |

레코드가 위와 같다고 가정한다.

username = 검색

```python
>>> peter = User.query.filter_by(username='peter').first()
>>> peter.id
1
>>> peter.email
u'peter@example.org'
```

username = 검색 (존재하지 않으면 None을 반환)

```python
>>> missing = User.query.filter_by(username='missing').first()
>>> missing is None
True
```

email LIKE 검색

```python
>>> User.query.filter(User.email.endswith('@example.com')).all()
[<User u'admin'>, <User u'guest'>]
```

ORDER BY

```python
>>> User.query.order_by(User.username)
[<User u'admin'>, <User u'guest'>, <User u'peter'>]
```

LIMIT

```python
>>> User.query.limit(1).all()
[<User u'admin'>]
```

PK로 구하기

```python
>>> User.query.get(1)
<User u'admin'>
```

### 뷰에서 질의

```get_or_404``` 또는 ```first_or_404``` 헬퍼 함수를 사용하면 편리하다.

```python
@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)
```
