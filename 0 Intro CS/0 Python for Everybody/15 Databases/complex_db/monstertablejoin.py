import sqlite3
import os

os.chdir("15 Databases/complex_db")

conn = sqlite3.connect("complex_db.sqlite")
cur = conn.cursor()

for row in cur.execute(
        "select Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id"
):
    print("Title:", row[0], "\nArtist:", row[1], "\nAlbum", row[2], "\nGenre:",
          row[3], "\n")

cur.close()