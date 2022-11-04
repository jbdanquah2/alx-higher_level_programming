-- list all shows by their rating
SELECT
	ts.title,
	SUM(sr.rate) AS rating
	FROM tv_shows ts
	INNER JOIN tv_show_ratings sr 
		ON ts.id = sr.show_id
	GROUP BY ts.title
ORDER BY rating DESC;
