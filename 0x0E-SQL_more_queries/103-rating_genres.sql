-- list all genres by rating
SELECT
	tg.name,
	SUM(sr.rate) as rating
	FROM tv_genres tg
	JOIN tv_show_genres sg
		ON tg.id = sg.genre_id
	JOIN tv_shows ts
		ON ts.id = sg.show_id
	JOIN tv_show_ratings sr
		ON ts.id = sr.show_id
	GROUP BY tg.name
ORDER BY rating DESC;
