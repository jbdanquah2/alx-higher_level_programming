-- lists all shows without Comedy genre
SELECT DISTINCT 
	ts.title
	FROM tv_shows ts
	LEFT JOIN tv_show_genres sh
		ON ts.id = sh.show_id 
	LEFT JOIN tv_genres tg
		ON tg.id = sh.genre_id
	WHERE ts.title 
	NOT IN (SELECT DISTINCT
			ts.title
		FROM tv_shows ts
		JOIN tv_show_genres sh
			ON ts.id = sh.show_id
		JOIN tv_genres tg
			ON tg.id = sh.genre_id
		WHERE tg.name = 'Comedy')
ORDER BY ts.title ASC;
