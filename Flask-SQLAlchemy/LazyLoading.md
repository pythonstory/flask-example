# FK 선언만 하는 경우 = 참조변수 있음(lazy 옵션 지정 안함 디폴트)

```python
p = Post.query.first()
```

```sql
SELECT post.id, post.title, post.body, post.pub_date, post.category_id 
FROM post
```

```python
c = Category.query.first()
```

```sql
SELECT category.id, category.name
FROM category
```

# Post 모델에서 category 선언 참조

## category = db.relationship('Category')

```python
p = Post.query.first()
```

```sql
SELECT post.id, post.title , post.body , post.pub_date, post.category_id 
FROM post
```

```python
p.category
```

```sql
SELECT category.id, category.name
FROM category
```

## category = db.relationship('Category', lazy='immediate')

- immediate, select, subquery 2.1.과 동일

## category = db.relationship('Category', lazy='joined')

```python
category = db.relationship('Category') 
```

```sql
SELECT post.id, post.title , post.body , post.pub_date, post.category_id, category.id, category.name
FROM post LEFT OUTER JOIN category ON category.id = post.category_id
```

## category = db.relationship('Category', lazy='dynamic')

```python
category = db.relationship('Category')
```

에러: On relationship Post.category, 'dynamic' loaders cannot be used with many-to-one/one-to-one relationships and/or uselist=False.

# ```Category``` 모델에서 ```post``` 참조 선언

## posts = db.relationship('Post')

```python
c = Category.query.first()
```

```sql
SELECT category.id, category.name
FROM category
```

```python
c.posts
```

```sql
SELECT post.id, post.title, post.body, post.pub_date, post.category_id
FROM post 
WHERE ? = post.category_id
```

## posts = db.relationship('Post', lazy='dynamic')

- dynamic, immediate, select 3.1.과 동일

```python
c = Category.query.first()
```

```sql
SELECT category.id, category.name
FROM category
```

```python
c.posts
```

```sql
SELECT post.id, post.title, post.body, post.pub_date, post.category_id
FROM post 
```

## category = db.relationship('Category', lazy='subquery')

```python
c = Category.query.first()
```

```sql
SELECT category.id AS category_id, category.name
FROM category
```

```python
c.posts
```

```sql
SELECT post.id, post.title, post.body, post.pub_date, post.category_id, t.category_id
FROM (SELECT category.id
FROM category) AS t JOIN post ON t.category_id = post.category_id ORDER BY t.category_id
```

## category = db.relationship('Category', lazy='joined')

```python
c = Category.query.first()
```

```sql
SELECT t.category_id, t.category_name, post.id, post.title, post.body, post.pub_date, post.category_id
FROM (SELECT category.id, category.name
FROM category) AS t LEFT OUTER JOIN post AS post ON t.category_id = post.category_id
```

```python
c.posts
```

추가 질의 없이 결과 반환

# ```backref```와 ```lazy``` 옵션 관계

```python
category = db.relationship('Category', backref=db.backref('posts', lazy='select'), lazy='dynamic')
```

```Post``` 모델 안에 ```category``` 변수 선언할 때 ```backref=db.backref('posts', lazy='select')``` 옵션을 이렇게 지정하는 것은 ```Category``` 모델 안에 ```post``` 변수를 ```db.relationship('Post', lazy='select')```와 같이 선언하는 것과 같다.