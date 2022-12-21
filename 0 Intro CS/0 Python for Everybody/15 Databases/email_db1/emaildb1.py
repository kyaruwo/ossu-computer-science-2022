import sqlite3
import os

os.chdir("15 Databases/emaildb1")

conn = sqlite3.connect("emaildb1.sqlite")
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
except:
    cur.execute("DELETE FROM Counts")

fh = open("mbox.txt")

i = 1
for line in fh:
    if line.startswith("From: "):
        pieces = line.split()
        email = pieces[1].split("@")
        org = email[1]
    else:
        continue

    cur.execute("SELECT count FROM Counts WHERE org = ?", (org, ))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org, ))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",
                    (org, ))

    if i > 10:
        conn.commit()
        i = 1
conn.commit()

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()