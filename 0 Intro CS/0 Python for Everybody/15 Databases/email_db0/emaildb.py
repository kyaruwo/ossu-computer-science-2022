import sqlite3
# :>
import os

os.chdir("15 Databases/emaildb0")
#hange directory because vscode kept executing the python file into the root folder of the current open folder:>

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()
#delete the table if it exist
cur.execute("DROP TABLE IF EXISTS Counts")
try:
    cur.execute("CREATE TABLE Counter (email TEXT, count INTEGER)")
except:
    None

while True:
    try:
        #mbox-short.txt
        fname = input("Enter file name: ")
        fh = open(fname)
    except:
        print("file cannot be found, ", fname)
        continue
    break

i = 1
for line in fh:
    if line.startswith("From: "):
        pieces = line.split()
        email = pieces[1]
    else:
        continue

    #the "?" inside the sql command is to avoid sql injection
    cur.execute("SELECT count FROM Counter Where email = ?", (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counter (email, count) VALUES (?, 1)",
                    (email, ))
    else:
        cur.execute("UPDATE Counter SET count = count + 1 WHERE email = ?",
                    (email, ))

    #this is to save time because .commit is slow; instead of commiting every line we commit per 10 lines
    i += 1
    if i > 10:
        conn.commit()
#this is to commit the uncomited lines after the loops
conn.commit()

sqlstr = "SELECT email, count FROM Counter ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()