from random import shuffle
import re


class Song:
    def __init__(self, name, artist, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = int(year)
        self.duration = int(duration)

    def __repr__(self):
        song = "Song \"%s\" by %s from album \"%s\" (%d) - position %s, %d" % (self.name, self.artist, self.album, self.year, self.position, self.duration)
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def import_songs(input_file):
    with open(input_file, 'r') as fh:
        songs = []
        for line in input_file:
            line.rstrip()
            songs.append(Song(*line.split('\t')))
    return songs


def export_songs(songs, target_file):
    with open(target_file, 'w') as ofile:
        for song in songs:
            ofile.write('\t'.join([song.name, song.artist, song.album, song.position, str(song.year), str(song.duration)]) + '\n')


def shuffle_songs(songs):
    shuffle(songs)
    return songs


# Most frequent artist
counts = {}
for song in songs:
    artist_name = song.artist
    counts[artist_name] = counts.get(artist_name, 0) + 1
max_count = None
for artist_name, count in counts.items():
    if max_count is None or count > max_count:
        popular = artist_name
        max_count = count
print(popular)


# Longest song
max_length = None
for song in songs:
    if max_length is None or song.duration > max_length:
        long_song = (song.name, song.artist)
        max_length = song.duration
print("\t".join(long_song))


# Longest album
album_lengths = {}
for song in songs:
    key = song.album + "\t" + song.artist
    album_lengths[key] = album_lengths.get(key, 0) + song.duration
max_duration = None
for album, duration in album_lengths.items():
    if max_duration is None or duration > max_duration:
        our_victim = album
        max_duration = duration
print(our_victim)


# Most frequent word
words = {}
for song in songs:
    song_words = re.findall('[a-zA-Z]+', song.name)
    for word in song_words:
        word = word.lower()
        words[word] = words.get(word, 0) + 1
word_counts = sorted([(x[1], x[0]) for x in list(words.items())], reverse=True)
num_words = 10 if len(word_counts) > 10 else len(word_counts)
print("\t".join([x[1].lower() for x in word_counts[:num_words]]))


# Highest album count
album_counts = {}
for song in songs:
    album_counts[song.artist] = album_counts.get(song.artist, []) + [song.album]
max_count = None
for artist, albums in album_counts.items():
    albums = set(albums)
    if max_count is None or len(albums) > max_count:
        cool_artist = artist
        max_count = len(albums)
print(cool_artist)
