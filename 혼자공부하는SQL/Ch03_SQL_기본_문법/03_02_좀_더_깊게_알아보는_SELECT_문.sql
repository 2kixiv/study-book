-- [ 핵심 키워드 ] ORDER BY / LIMIT / DISTINCT / GROUP BY / HAVING

-- ORDER BY
SELECT mem_id, mem_name, debut_date
    FROM member
    ORDER BY debut_date ASC;

SELECT mem_id, mem_name, debut_date
    FROM member
    ORDER BY debut_date DESC;

SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height >= 164
    ORDER BY height DESC;

SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height >= 164
    ORDER BY height DESC, debut_date ASC;

-- LIMIT
SELECT * FROM member LIMIT 3;

SELECT mem_name, debut_date
	FROM member
    ORDER BY debut_date
    LIMIT 3;

SELECT mem_name, height
	FROM member
    ORDER BY height DESC
    LIMIT 3, 2;

-- DISTINCT
SELECT DISTINCT addr FROM member;

-- 집계 함수
/*
SUM()
AVG()
MIN()
MAX()
COUNT()
COUNT(DISTINCT)
*/
SELECT AVG(amount) "평균 구매 개수" FROM buy;
SELECT COUNT(phone1) "연락처가 있는 회원" FROM member;

-- GROUP BY
SELECT mem_id, SUM(amount) FROM buy GROUP BY mem_id;
SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수" FROM buy GROUP BY mem_id;
SELECT mem_id "회원 아이디", SUM(price * amount) "총 구매 금액" FROM buy GROUP BY mem_id;
SELECT mem_id, AVG(amount) "평균 구매 개수" FROM buy GROUP BY mem_id;

-- HAVING
SELECT mem_id "회원 아이디", SUM(price * amount) "총 구매 금액"
	FROM buy GROUP BY mem_id
    HAVING SUM(price * amount) > 1000;

SELECT mem_id "회원 아이디", SUM(price * amount) "총 구매 금액"
	FROM buy GROUP BY mem_id
    HAVING SUM(price * amount) > 1000
    ORDER BY SUM(price * amount) DESC;