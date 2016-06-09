# 관계

## 일대다(one-to-many)


### 참조키 정의

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
    
* ```db.create_all()``` 호출로 Post(id, title, category_id) 테이블과 Category(id, name) 테이블을 만든다.
* ```Post``` 테이블의 ```category_id``` 참조키 필드는 정의하고 있으나 어떠한 관계도 정의하고 있지 않다.
    * ```post.category```, ```category.posts``` 같은 사용은 불가능하다.
 
### 일대다 관계 (양방향)

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

* ```posts = db.relationship('Post')```로 일대다/다대일 양방향(bidirectional) 관계를 정의한다.
    * ```post.category``` 형태로 Category를 가져올 수 있다.
    * ```category.posts``` 형태로 Post 리스트를 가져올 수 있다.
    
### 일대다 관계 (역참조 변수 추가)

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
    posts = db.relationship('Post', backref='category')
```

* ```backref``` 속성으로 역참조 변수를 추가해 모델 클래스 한 쪽에만 참조변수를 선언할 수 있다.
    * 여전히 ```post.category```, ```category.posts``` 형태로 레코드를 가져올 수 있다.
    
