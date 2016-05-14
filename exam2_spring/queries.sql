-- Ordered users
select * from Users order by username;

-- Latest 5
select * from Users order by registered desc limit 5;

-- Top 5 zadrots
select Users.username, count(*) as cnt from Users inner join Listened on Users.id = Listened.user_id group by Users.username order by cnt desc limit 5;

-- Albums number
select Artists.name, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id group by Artists.id order by cnt desc;

-- Songs number
select Artists.name, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Artists.id order by cnt desc limit 1;

-- Longest by count
select Artists.name, Albums.name, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Albums.id order by cnt desc limit 1;

-- Longest by duration
select Artists.name, Albums.name, total(duration) as sd from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Albums.id order by sd desc limit 1;

-- Biggest average
select Artists.name, Albums.name, total(duration)/count(*) as avg from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id group by Albums.id order by avg desc limit 1;

-- Most listened
select Artists.name, Albums.name, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id inner join Listened on Listened.song_id = Songs.id group by Songs.id order by cnt desc limit 5;

-- Year of most listened
select Albums.release_year, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id inner join Listened on Listened.song_id = Songs.id group by Albums.release_year order by cnt desc limit 1;

-- 20 last listened for number 47!
select Artists.name, Albums.name, Songs.name, Listened.start_time from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id inner join Listened on Listened.song_id = Songs.id inner join Users on Users.id = Listened.user_id where Users.id = 47 order by Listened.start_time desc limit 20;

-- I can't even understand why the fuck. Anyway.
select Users.username, Artists.name, Albums.name, Songs.name, count(*) as cnt from Artists inner join Albums on Artists.id = Albums.artist_id inner join Songs on Songs.album_id = Albums.id inner join Listened on Listened.song_id = Songs.id inner join Users on Users.id = Listened.user_id group by Users.id, Songs.id order by cnt desc;
