-- [ 핵심 키워드 ] 인덱스 / 뷰 / 스토어드 프로시저

-- 인덱스 생성
CREATE INDEX idx_member_name ON member(member_name);

-- 뷰 생성
CREATE VIEW member_view AS SELECT * FROM member;

-- 뷰 접근
SELECT * FROM member_view;

-- 스토어드 프로시저 생성
DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
	SELECT * FROM member WHERE member_name = '나훈아';
	SELECT * FROM product WHERE product_name = '삼각김밥';
END //
DELIMITER ;

-- 스토어드 프로시저 호출
CALL myProc();