-- Ranks country origins of bands, ordered by the number of (non-unique)
-- fans


-- Select country of origin
SELECT * origin, SUM(nb_fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
