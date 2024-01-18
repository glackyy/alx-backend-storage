-- A Script that selects band_name, lifespan column

SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('GLAM ROCK', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC