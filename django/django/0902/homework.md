# HomeWork

1. ```
   python manage.py makemigrations
   설계도를 만든다
   python manage.py migrate
   이 마이그레이션을 DB에 반영한다.
   ```

2. ```
   3번 
   post=Post(title="제목",content="내용")
   post.save()
   로 변경해줘야한다.
   ```

3. ```
   2번이 실행하지 않는다
   -> 음수 인덱스는 지원하지 않는다.
   ```

4. ```
   my_post.title ="안녕하세요"
   my_post.content ="반갑습니다"
   my_post.save()
   ```

5. ```
   posts =Post.object.all()
   ```

