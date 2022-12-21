import sqlite3
import os

os.chdir("15 Databases/Tracks")

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

for row in cur.execute(
        "select Track.title, Album.title, Artist.name  from Track join Album join Artist on Track.album_id = Album.id and Album.artist_id = Artist.id"
):
    print(row[0], row[1], row[2])

cur.close()