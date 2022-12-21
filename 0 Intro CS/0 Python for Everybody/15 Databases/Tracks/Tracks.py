import sqlite3 as sql
import xml.etree.ElementTree as xml
import os

os.chdir("15 Databases/Tracks")

#sqlite

conn = sql.connect("trackdb.sqlite")
cur = conn.cursor()

#create a table and add a column of autoincrement id of integers that is unique
cur.executescript("""
    drop table if exists Artist;
    drop table if exists Album;
    drop table if exists Track;

    create table Artist (id integer not null primary key autoincrement unique,
    name text unique);

    create table Album (id integer not null primary key autoincrement unique,
    title text unique,
    artist_id integer
    );

    create table Track (id integer not null primary key autoincrement unique,
    title text unique,
    album_id integer,
    len integer,
    rating integer,
    count integer
    );
    """)

#xml crawler


def lookup(d, key):
    found = False
    #d = <dict>{<key><value>,...} we are iterating the {<key><value>,...}
    #{(<dict>(<key></key><value></value>)...</dict>)...}
    for child in d:
        if found:
            #return the value of the key
            return child.text
        #check if the tag is equal to "key" and if the value of the key tag is equal to the key
        if child.tag == "key" and child.text == key:
            found = True
    #return None if there is no "Track ID" key
    return None


#XML

fname = "Library.xml"

file = xml.parse(fname)

data = file.findall("dict/dict/dict")
#data = {dict:{key,...},...}
#{<dict><dict>(<dict>(<key></key><value></value>)...</dict>)...</dict></dict>}
print("dict count:", len(data))

for entry in data:
    #data = {dict{key,...},...} we are iterating the dict{key,...}
    #{(<dict>(<key></key><value></value>)...</dict>)...}
    if (lookup(entry, "Track ID") is None):
        continue

    #return the values of the "keys"; Name, Artist, Album, Play Count, Rating, Total Time
    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    #if name, artist, album is None continue, just sanity check by chuck
    if name is None or artist is None or album is None:
        continue
    else:
        #print the data
        print("title:", name, "artist:", artist, "album:", album, "playcount:",
              count, "rating:", rating, "length:", length)

    #Databases

    #insert artist into Artist table
    #ignore or skip if the unique parameter of the table is violated
    cur.execute("insert or ignore into Artist (name) values (?)", (artist, ))
    #pull the artist_id
    cur.execute("select id from Artist where name = ?", (artist, ))
    artist_id = cur.fetchone()[0]

    #insert album name and artist_id into Album table
    #ignore or skip if the unique parameter of the table is violated
    cur.execute("insert or ignore into Album (title, artist_id) values (?, ?)",
                (album, artist_id))
    #pull the album_id
    cur.execute("select id from Album where title = ?", (album, ))
    album_id = cur.fetchone()[0]

    #insert title, length, rating, count, album_id into Track table
    #replace or update the columns of the rows of the table
    cur.execute(
        "insert or replace into Track (title, len, rating, count, album_id) values (?, ?, ?, ?, ?)",
        (name, length, rating, count, album_id))
    #transfer the changes from the ram into the database file
    conn.commit()

cur.close()