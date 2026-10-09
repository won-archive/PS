-- 코드를 입력하세요
-- 입양을 간 동물 중 -> JOIN
-- 보호 기간이 가장 길었던 동물 두 마리
-- 아이디, 이름 조회
-- 보호 기간이 긴 순

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON O.ANIMAL_ID = I.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2