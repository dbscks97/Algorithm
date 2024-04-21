-- 모든 시간(0시부터 23시까지)에 대한 더미 테이블을 생성
WITH RECURSIVE Hours AS (
    SELECT 0 AS Hour
    UNION ALL
    SELECT Hour + 1 FROM Hours WHERE Hour < 23
)

-- 더미 테이블과 ANIMAL_OUTS를 조인하여 모든 시간대에 대한 데이터를 표시
SELECT
    h.Hour,
    COUNT(a.DATETIME) AS COUNT
FROM
    Hours h
LEFT JOIN
    ANIMAL_OUTS a ON h.Hour = HOUR(a.DATETIME)
GROUP BY
    h.Hour
ORDER BY
    h.Hour;
