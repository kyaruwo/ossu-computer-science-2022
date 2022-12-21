import sqlite3
import os

os.chdir("15 Databases/complex_db")

conn = sqlite3.connect("complex_db.sqlite")
cur = conn.cursor()


def nav(nav):
    if nav == "quit":
        quit()
    elif nav == "return":
        main()


#note to do; compact the for loops
def title_search():
    x = False
    while True:
        title = input("\nEnter title: ")
        nav(title)

        for i in cur.execute(
                "SELECT id, title, album_id FROM Track ORDER BY id ASC"):
            if i[1] != title:
                continue
            else:
                print("\nSong:", i[1])
                x = True

            for j in cur.execute(
                    "SELECT id, title, artist_id FROM Album ORDER BY id ASC"):
                if j[0] == i[2]:
                    print("Album Title:", j[1])
                else:
                    continue

                for k in cur.execute(
                        "SELECT id, name FROM Artist ORDER BY id ASC"):
                    if k[0] == j[2]:
                        print("Artist:", k[1])
                    else:
                        continue
                    break
                break
            break
        break

    if x != True:
        print("No such title found")
        title_search()
    elif x == True:
        cur.close()


def artist_search():
    x = False
    while True:
        artist = input("\nEnter artist: ")
        nav(artist)

        for i in cur.execute("SELECT id, name FROM Artist ORDER BY id ASC"):
            if i[1] != artist:
                continue
            else:
                print("\nArtist:", i[1])
                x = True

            for j in cur.execute(
                    "SELECT id, title, artist_id FROM Album ORDER BY id ASC"):
                if j[2] != i[0]:
                    continue
                else:
                    print("Album Title:", j[1])

                for k in cur.execute(
                        "SELECT id, title, album_id FROM Track ORDER BY id ASC"
                ):
                    if k[2] != j[0]:
                        continue
                    else:
                        try:
                            print("Song:", k[1])
                            continue
                        except:
                            None
                    break
                break
            break
        break

    if x != True:
        print("No such title found")
        artist_search()
    elif x == True:
        cur.close()


def album_search():
    x = False
    while True:
        album = input("\nEnter Album: ")
        nav(album)

        for i in cur.execute(
                "SELECT id, title, artist_id FROM Album ORDER BY id ASC"):
            if i[1] != album:
                continue
            else:
                print("\nAlbum:", i[1])
                x = True

            for j in cur.execute(
                    "SELECT id, name FROM Artist ORDER BY id ASC"):
                if j[0] != i[2]:
                    continue
                else:
                    print("Artist:", j[1])

            for k in cur.execute(
                    "SELECT id, title, album_id FROM Track ORDER BY id ASC"):
                if k[2] != i[0]:
                    continue
                else:
                    try:
                        print("Song:", k[1])
                        continue
                    except:
                        None
                break
            break
        break

    if x != True:
        print("No such title found")
        album_search()
    elif x == True:
        cur.close()


def main():
    conn = sqlite3.connect("complex_db.sqlite")
    cur = conn.cursor()
    while True:
        stype = input(
            "\nChoose Search Type: \"title\", \"artist\", \"album\" : ")

        if stype == "quit":
            quit()
        elif stype == "title":
            title_search()
        elif stype == "artist":
            artist_search()
        elif stype == "album":
            album_search()
        else:
            print("    ==== Invalid Search Type ====    ")
            continue


print("Enter \"quit\" to exit; \"return\" to go back, \"case sensitive\"")

main()