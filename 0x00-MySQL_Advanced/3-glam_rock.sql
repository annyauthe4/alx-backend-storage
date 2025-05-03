-- Lists all bands with Glam_rock as their main style, ranked by
-- longevity.


-- Select attributes
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
