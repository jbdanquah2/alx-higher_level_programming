-- counts the number of records with same scores
SELECT score, COUNT(1) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
