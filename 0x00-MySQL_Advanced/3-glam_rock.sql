-- Lists all bands with Glam_rock as their main style, ranked by
-- longevity.


-- List attributes
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
