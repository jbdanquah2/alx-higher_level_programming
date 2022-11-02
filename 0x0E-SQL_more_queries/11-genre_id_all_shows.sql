-- list all tv shows and gener id
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
