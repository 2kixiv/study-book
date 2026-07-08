-- [ 핵심 키워드 ] INSERT / AUTO_INCREMENT / INTER INTO ~ SELECT / UPDATE / DELETE

-- INSERT
USE market_db;
CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);
INSERT INTO hongong1 VALUES (1, '우디', 25);
INSERT INTO hongong1 (toy_id, toy_name) VALUES (2, '버즈');
INSERT INTO hongong1 (toy_name, age, toy_id) VALUES ('제시', 20, 3);

-- AUTO INCREMENT
CREATE TABLE hongong2
(
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT
);

INSERT INTO hongong2 VALUES (NULL, '보핖', 25);
INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES (NULL, '렉스', 21);
SELECT LAST_INSERT_ID(); -- 3

ALTER TABLE hongong2 AUTO_INCREMENT = 100;
INSERT INTO hongong2 VALUES (NULL, '재남', 35);
SELECT LAST_INSERT_ID(); -- 100


CREATE TABLE hongong3
(
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT
);

ALTER TABLE hongong3 AUTO_INCREMENT = 1000;
SET @@auto_increment_increment = 3;

INSERT INTO hongong3 VALUES (NULL, '토마스', 20);
INSERT INTO hongong3 VALUES (NULL, '제임스', 23);
INSERT INTO hongong3 VALUES (NULL, '고든', 25);
SELECT LAST_INSERT_ID(); -- 1006

-- 시스템 변수
SHOW GLOBAL VARIABLES; -- 전체 시스템 변수 조회
SELECT 시스템변수; -- 시스템 변수 값 조회
SET 시스템 변수; -- 시스템 변수 설정

-- 테이블 구조 확인
DESC world.city;

-- INSERT INTO ~ SELECT
CREATE TABLE city_popul (city_name CHAR(35), population INT);
INSERT INTO city_popul SELECT Name, Population FROM world.city;

-- UPDATE
UPDATE city_popul SET city_name = '서울' WHERE city_name = 'Seoul';
UPDATE city_popul
    SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
UPDATE city_popul SET population = population / 10000;

-- DELETE
DELETE FROM city_popul WHERE city_name LIKE 'New%';
DELETE FROM city_popul WHERE city_name LIKE 'New%' LIMIT 5;

DELETE FROM big_table1; -- 테이블 안의 행만 삭제, 한 행씩 삭제해서 시간이 오래 걸림
DROP TABLE big_table2; -- 테이블 자체를 삭제
TRUNCATE TABLE big_table3; -- 테이블 안의 행을 한번에 삭제, 연산 빠름