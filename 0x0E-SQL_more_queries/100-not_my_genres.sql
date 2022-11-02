-- list all genres not linked to Dexter
SELECT
	DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
	on tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title <> "Dexter"
ORDER BY tv_genres.name ASC;
