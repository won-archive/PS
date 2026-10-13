-- 코드를 입력하세요
-- 생일이 3월인 여성 회원
-- ID, 이름, 성별, 생년월일을 조회
-- 전화번호가 NULL인 경우 제외
-- 회원ID를 기준으로 오름차순
-- DATE_OF_BIRTH의 데이트 포맷이 예시와 동일해야 정답

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 AND GENDER = 'W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID