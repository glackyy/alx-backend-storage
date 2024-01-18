-- A Script that selects origin column, and sum of fans
-- grouped by origin and ordered by num of fans desc

SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
