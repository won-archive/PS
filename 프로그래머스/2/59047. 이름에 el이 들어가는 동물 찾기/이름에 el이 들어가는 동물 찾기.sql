-- 코드를 입력하세요
-- 이름에 'EL' 들어가는 개의
-- 아이디, 이름 조회
-- 순서: 이름 순 -> 아이디 순 
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME, ANIMAL_ID