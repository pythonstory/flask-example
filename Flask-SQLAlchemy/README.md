# Flask-SQLAlchemy

[Flask-SQLAlchemy 공식문서](http://flask-sqlalchemy.pocoo.org/2.1/)

## 연동 설정

소스: [Flask-SQLAlchemy/01-config](01-config)

* ```SQLALCHEMY_DATABASE_URI```
    * ```sqlite:////absolute/path/to/foo.db```
    * ```mysql://scott:tiger@localhost/mydatabase```
    * ```oracle://scott:tiger@127.0.0.1:1521/sidname```
    * ```postgresql://scott:tiger@localhost/mydatabase```
* ```SQLALCHEMY_TRACK_MODIFICATIONS```
    * 2.1 버전부터는 명시적으로 False로 지정할 것
    
## 모델 정의

### User 모델 정의 예시

소스: [Flask-SQLAlchemy/02-user-model](02-user-model)

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

* 모델 컬럼 타입

| 타입 이름 | 파이썬 타입 | 설명 |
|-----------|-------------|------|
| Integer | int | 32비트 정수 |
| SmallInteger | int | 16비트 정수 |
| BigInteger | int or long | 무제한 길이 정수 |
| Float | float | 부동소수 |
| BigDecimal | decimal.Decimal | 고정소수 |
| String | str | 가변길이 문자열 |
| Text | str | 가변길이 문자열, 대용량 |
| Unicode | unicode | 가변길이 유니코드 문자열 |
| UnicodeText | unicode | 가변길이 유니코드 문자열, 대용량 |
| Boolean | bool | Boolean 값 |
| Date | datetime.date | 일자 |
| Time | datetime.time | 시각 |
| DateTime | datetime.datetime | 일자 시각 |
| Interval | datetime.timedelta | 시간 차이 |
| Enum | str | 문자열 값 리스트 |
| PickletType | 불특정 파이썬 객체 | 자동 피클 직렬화 |
| LargeBinary | str | 이진 blob |

### 모델/뷰 파일 모듈로 분리 및 설정 클래스

소스: [Flask-SQLAlchemy/03-config](03-config)

* ```config``` 모듈 ```Configuration``` 클래스에 SQLAlchemy 관련 설정 멤버 변수 선언
* ```run.py```에 models를 임포트
* ```models.py``` 파일을 새로 만들어 필요한 모델 정의
* ```__init__.py```에 SQLAlchemy db 객체 선언
* ```from run import db``` 임포트로 ```db.create_all()``` 호출
    * ```db.create_all()``` 호출하기 전에 반드시 모델이 먼저 임포트되어 있어야 한다.

## 관계 정의

### 다대일 관계

소스: [Flask-SQLAlchemy/04-many-to-one](04-many-to-one)

1. 파이썬 객체 생성 - 참조되는 객체를 먼저 생성
1. Flask-SQLAlchemy 세션에 추가 - 참조되는 객체를 먼저 추가
1. Flask-SQLAlchemy 세션을 커밋

```python
>>> from hello import db, Post, Category
>>> Post.query.all()
[]
>>> c = Category('python')
>>> p = Post('Hello Python', 'Python is cool', c)
>>> db.session.add(c)
>>> db.session.add(p)
>>> db.session.commit()
>>> c.posts
<sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x1027d37d0>
>>> c.posts.all()
[<Post 'Hello Python'>]
>>> p.category
<Category 'python'>
```

* 관계 정의 옵션

| 옵션 이름 | 설명 |
|-----------|------|
| backref | 관계를 맺어 다른 모델의 역참조를 추가 |
| primaryjoin | 두 모델 사이에 조인 조건을 명시적으로 지정<br>관계가 불명확할 때에만 필요 |
| lazy | select <br> immediate <br> joined <br> subquery <br> noload <br> dynamic |
| uselist | False일 경우 리스트가 아니라 스칼라(객체) - 일대일 제약조건으로 사용 |
| order_by | 관계에서 항목의 순서를 지정 |
| secondary | 다대다 관계에서 연관 테이블의 이름을 지정 |
| secondaryjoin | 관계가 불분명할 때 다대다 관계에서 2차 조인 조건을 지정 |

### 다대다 관계

소스: [Flask-SQLAlchemy/05-many-to-many](04-many-to-many)

* 연관 테이블의 선언을 실제 모델에서 참조하기 전에 선언해야 한다.
* lazy 옵션을 양방향 모두 dynamic으로 하면 실체 반환되는 참조 객체에서 all() 메소드를 체인해야 쿼리 결과를 얻을 수 있다.

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
