# 관계

## 일대다(one-to-many, 1:N)

### 참조키 선언

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    # Category 모델 참조키
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
```
    
* ```db.create_all()``` 호출로 post(id, title, category_id) 테이블과 category(id, name) 테이블을 만든다.
    * ```Category```:```Post``` 관계는 1:N (one-to-many, 일대다)이다.
* ```Post``` 테이블의 ```category_id``` 참조키 필드는 선언하고 있으나 _어떠한 관계도 선언하고 있지 않다_.
    * ```post.category```, ```category.posts``` 같은 사용은 불가능하다.
 
### 일대다 관계 선언(양방향)

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    # Category 모델 참조키
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    # Category 참조 변수
    category= db.relationship('Category')
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    # Post 리스트 참조 변수
    posts = db.relationship('Post')
```

* ```posts = db.relationship('Post')```로 일대다/다대일 양방향(bidirectional) 관계를 선언한다.
    * ```post.category``` 형태로 Category를 가져올 수 있다.
    * ```category.posts``` 형태로 Post 리스트를 가져올 수 있다.
* 양방향(bidirectional)이 아니라 단방향(unidirectional)을 구현하려면 필요 없는 모델 클래스 안에 참조변수를 선언하지 않는다.
    * 일반적으로는 참조키를 두는 쪽에서 참조 변수를 선언한다. 위 예시에서는 ```Post``` 모델 클래스에서만 ```db.relationship()``` 선언을 하는 것이다.
    
### 일대다 관계 선언 (양방향 but 역참조 변수 추가로 한 쪽에만 선언)

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    # Category 모델 참조키
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    # Category 참조 변수
    category = db.relationship('Category', backref='posts')
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
```

* ```backref``` 속성으로 역참조 변수를 추가해 모델 클래스 한 쪽에만 참조변수를 선언할 수 있다.
    * 여전히 ```post.category```, ```category.posts``` 형태로 레코드를 가져올 수 있다.
    
### 일대일 관계
    
```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    # Category 모델 참조키
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    # Post 리스트 참조 변수
    post = db.relationship('Post', backref='category', uselist=False)
```

* 원래 하나의 Category에 대하여 N개의 Post가 존재할 수 있는 관계에서 ```uselist=False``` 제약으로 리스트가 아닌 하나의 스칼라만 가져오도록 할 수 있다.
    * 변수명도 ```posts```가 아닌 ```post``` 단수형으로 선언하는 것이 타당하다.

## 다대다(many-to-many, M:N)

### 참조키 선언

```python
post_tags = db.Table('post_tags', 
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
```

* ```db.create_all()``` 호출로 post(id, title) 테이블과 tag(id, name) 테이블, post_tags(tag_id, post_id) 연관 테이블을 만든다.
    * ```Post``` 테이블과 ```Tag``` 관계는 연관 테이블을 통해서 M:N (many-to-many, 다대다)이다.
* ```post_tags``` 테이블에서 ```tag_id```와 ```post_id``` 참조키 필드를 선언하고 있으나 _어떠한 관계도 선언하고 있지 않다_.
    * ```post.tags```, ```tag.posts``` 같은 사용은 불가능하다.

### 다대다 관계 선언(양방향)

```python
post_tags = db.Table('post_tags', 
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
```

* ```post_tags``` 연관 테이블은 ```Post``` 모델 안에서 ```post_tags``` 이름으로 변수 참조하기 때문에 ```Post``` 모델 선언보다 위에 있어야 한다.
    * ```post_tags``` 테이블 선언이 아래에 있으면 이름이 정의되어 있지 않다(name is not defined)는 에러가 발생한다.
* ```Post``` 모델 안에 ```tags``` 변수가 선언되어 있고 backref 역참조 속성을 ```posts``` 변수 이름으로 지정하고 있다.
    * ```post.tags``` 및 ```tag.posts``` 양방향 참조가 가능하다.

# lazy 옵션

```python
    # Category 리스트 참조 변수
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))
```

* ```Category``` 모델이 ```Post```를 역참조할 때 ```lazy='dynamic'```이 의미가 있다.
* ```Post``` 모델은 1:N으로 가져오기 때문에 무조건 하나의 쿼리(single query)로 조인(join)한다.
    * ```category = db.relationship('Category', backref='posts', lazy='dynamic')``` 문장은 에러가 발생한다.
    * 참조하는 쪽에서는 참조되는 모델의 데이터를 사용해야할 가능성이 높고 하나의 레코드만 가져오므로 오버헤드가 크지 않기 때문에 강제로 조인한다.
    * 만약 참조 변수를 ```Category``` 모델에 두고 ```posts = db.relationship('Post', lazy='immediate') 코드로 해야 레코드를 가져온다.