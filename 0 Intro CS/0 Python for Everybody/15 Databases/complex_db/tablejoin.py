import sqlite3
import os

os.chdir("15 Databases/complex_db")

conn = sqlite3.connect("complex_db.sqlite")
cur = conn.cursor()

#table for album and artist
for i in cur.execute(
        "select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id"
):
    print("Album: \"", i[0], "\" by", i[1])
#table for songs and album
for j in cur.execute(
        "select Track.title, Album.title from Track join Album on Track.album_id = Album.id;"
):
    print("Song: \"", j[0], "\" in", j[1], "Album")

cur.close()