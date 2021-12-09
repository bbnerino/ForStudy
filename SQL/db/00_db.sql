-- tutorial db 생성
sqlite3 tutorial.sqlite3 
-- table 확인
.tables
-- 현재 작업중인 database 저장 위치
.database
-- 창 청소
.shell cls

-- 모든 내용 조회
SELECT * FROM classmates;

-- CREATE TABLE
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- .tables -> table 목록 확인
-- .schema table_name
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- data CREATE
INSERT INTO classmates (name,age) 
VALUES ('홍길동',23);


INSERT INTO classmates (name,age,address)
VALUES ('홍길동',30,'서울');

-- 조회시 필요한 column 같이 작성
-- rowid 컬럼을 포함한 다름 모든 컬럼
SELECT rowid, * FROM classmates;
SELECT name FROM classmates;



CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
-- 만든지 확인
.schema classmates

INSERT INTO classmates 
(name, age, address)
VALUES ('홍길동',30,'서울');

INSERT INTO classmates 
(name, age, address)
VALUES ('김길동',30,'서울');

-- id 컬럼이 정의되어 있으므로
-- id를 직접 넣어줘야함
INSERT INTO classmates
VALUES(3,'한길동',20,'부산');

-- NOT NULL만 포함한 테이블 생성
CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 여러개의 데이터 한번에 집어넣기
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('임길동', 31, '부산'),
('이길동', 36, '대구'),
('박길동', 25, '대전'),
('최길동', 20, '울산');

-- name,age 만 가져오기
SELECT name,age FROM classmates;

-- name,age만 가져오기 + 3개만 조회하기
SELECT name,age FROM classmates
LIMIT 3;
-- 3번째의 값 하나 ->2개 빼고 한개 가져오기
SELECT name,age FROM classmates
LIMIT 1 OFFSET 2; 
-- name, age 칼럼 , 주소가 서울
SELECT * FROM classmates
WHERE address='서울';

-- 중복 제거 * 모든게 일치해야 걸러진다
SELECT DISTINCT * FROM classmates;

-- 6번 아이디 삭제
DELETE FROM classmates
WHERE rowid=5;

INSERT INTO classmates
VALUES ('김싸피', 30,'부산');

-- 1번 데이터의 이름을 '박싸피'로 
-- 나이를 100살로 수정
 
UPDATE classmates
SET name='박싸피', age=100
WHERE rowid=1;

CREATE TABLE users (
first_name TEXT Not NULL,
last_name TEXT Not NULL,
age INTEGER NOT NULL,
country TEXT Not NULL,
phone TEXT Not NULL,
balance INTEGER NOT NULL
);

-- csv에 대응할 수 있도록 mode 적용
.mode csv
-- csv 파일 불러온다
.import users.csv users

-- 데이터 전체조회
SELECT * FROM users;

-- users 테이블에서
-- age가 30 이상인 유저의 모든 컬럼 정보
SELECT * FROM users
WHERE age >= 30;
-- 이름만 출력!
SELECT first_name FROM users
WHERE age>=30;

-- age가 30이상이고 성이 '김' 인 사람의 
-- 나이와 성만 조회하려고 한다
SELECT age,last_name FROM users
WHERE age>= 30 AND last_name='김';

-- 나이가 30 이하거나 성이 '김' 인사람
SELECT * FROM users
WHERE age<=30 OR last_name='김'

-- users 테이블의 레코드 총 개수
SELECT COUNT(*) from users;

-- 나이의 평균값
SELECT AVG(age) FROM users;

-- 30살 이상인 사람들의 평균 나이는?
SELECT AVG(age) FROM users
WHERE age >=30;

-- 계좌잔액(BALANCE)가 가장 높은 사람의
-- 이름과 액수를 조회하려면
SELECT first_name,MAX(balance)
FROM users;

-- 30살이상의 평균 나이와
-- 평균 계좌 잔액
SELECT AVG(age),AVG(balance)
FROM users
WHERE age >= 30;

-- 30살 이하의 최소 계좌 잔액
SELECT first_name,MIN(balance) FROM users
WHERE age <=30;

-- LIKE
-- 나이가 20대인 사람만 조회한다면
SELECT * FROM users
WHERE age LIKE '2_';

-- 지역번호가 02인 사람만 조회
SELECT * FROM users
WHERE phone LIKE '02-%';

-- 이름이 '진'이거나 '준으로 끝나는 경우
SELECT first_name FROM users
WHERE first_name LIKE '%준'
OR first_name LIKE '%진';

-- ESCPE
SELECT * FROM escapes
WHERE text LIKE '^%%안녕'
ESCAPE '^';

-- 번호의 중간번호가 5114인 사람
SELECT * FROM users
WHERE phone LIKE '%-5114-____';

-- ORDER BY
-- 나이순으로 오름차순 정렬해서
-- 상위 10개만 조회
SELECT * FROM users
ORDER BY age ASC LIMIT 10;

-- 나이순, 성 순으로 오름차순 정렬해서
-- 상위 10개만 조회
SELECT * FROM users
ORDER BY age,last_name ASC LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬해서
-- 해당 유저의 성과 이름을
-- 10개만 조회 한다면?
SELECT last_name, first_name, balance
FROM users
ORDER BY balance DESC LIMIT 20;

SELECT last_name,COUNT(*)
FROM users
GROUP BY last_name;

-- 각 성씨가 몇명 있는지 조회 -> 컬럼명 변경
SELECT last_name,
COUNT(*) AS name_count
FROM users
GROUP BY last_name;

-- articles table new로 변경하기
ALTER TABLE articles
RENAME TO news;

-- 새로운 칼럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL
DEFAULT  'now';
-- default 에 넣으면 오류가 난다 -> 이렇게 바꾸기
INSERT INTO news
VALUES
('제목','내용', datetime('now'));

.headers on
.mode column

ALTER TABLE news
RENAME COLUMN created_at
TO updated_at;