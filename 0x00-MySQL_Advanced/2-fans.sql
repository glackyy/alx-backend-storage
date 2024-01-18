-- A Script that selects origin column, and sum of fans
-- grouped by origin and ordered by num of fans desc
SELECT origin, SUM(fans) AS numb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY numb_fans DESC