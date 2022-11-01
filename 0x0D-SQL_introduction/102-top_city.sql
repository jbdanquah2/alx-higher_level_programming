-- displays top 3 temperatures by city between July and August
SELECT city, avg(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
