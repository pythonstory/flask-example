# lazy 옵션 지정 안함 디폴트

```python
p = Post.query.first()
```

```sql
SELECT post.id, post.title, post.body, post.pub_date, post.category_id 
FROM post
```

```python
p.category
```

```sql
SELECT category.id, category.name
FROM category 
WHERE category.id = ?
```

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

## category = db.relationship('Category', lazy='select')

- select, immediate, subquery 디폴트와 동일

## category = db.relationship('Category', lazy='joined')

```python
p = Post.query.first()
```

```sql
SELECT post.id AS post_id, post.title AS post_title, post.body AS post_body, post.pub_date AS post_pub_date, post.category_id AS post_category_id 
FROM post
```

```python
p.cateogry
```

```sql
SELECT category.id, category.name, t.post_category_id
FROM (SELECT DISTINCT post.category_id
FROM post) AS t JOIN category ON category.id = t.post_category_id ORDER BY t.post_category_id
```

## category = db.relationship('Category', lazy='dynamic')

```python
p.category
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

## posts = db.relationship('Post', lazy='select')

- select, immediate 디폴트와 동일

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

## posts = db.relationship('Post', lazy='select')

디폴트, select, immediate와 동일하나 c.posts에서 all() 메소드를 체인해야 한다.

```python
c = Category.query.first()
```

```sql
SELECT category.id, category.name
FROM category
```

```python
c.posts.all()
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

# 정리

* 1:N에서 N인 곳에 lazy 옵션을 정의하는 경우
    * 디폴트 = select = immediate = subquery: SELECT 쿼리 2번
    * joined: 조인 쿼리 + SELECT
    * dynamic: 에러
* 1:N에서 1인 곳에 lazy 옵션을 정의하는 경우
    * 디폴트 = dynamic = select = immediate: SELECT 쿼리 2번
    * subquery: 서브쿼리 1번 + SELECT 쿼리
    * joined: JOIN 쿼리 1번 + 추가 쿼리 없이 반환
    
    
최종 결론

* 그냥 lazy 옵션을 지정하지 않고 만약에 성능상에 문제가 발생하면 그 때 최적화를 진행한다.
