-- 코드를 입력하세요
-- SEX_UPON_INTAKE = 'Neutered' or 'Spayed'
-- 아이디, 이름, 중성화 여부
-- 아이디 순
SELECT ANIMAL_ID, NAME,
    (CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%'
            OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
            ELSE 'X'
     END) AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID