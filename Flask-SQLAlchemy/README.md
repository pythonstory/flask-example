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
