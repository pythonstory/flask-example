# Flask-SQLAlchemy

[Flask-SQLAlchemy 공식문서](http://flask-sqlalchemy.pocoo.org/2.1/)

## 연동 설정

### 연동 설정

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

## 관계 정의

## CRUD
