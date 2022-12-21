import sqlite3
import json
import os

os.chdir("15 Databases/roster")

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

cur.executescript("""
    drop table if exists User;
    drop table if exists Course;
    drop table if exists Member;
    drop table if exists Role;

    create table User(
        id integer not null primary key autoincrement unique, 
        name text unique,
        email text
        );
    
    create table Course(
        id integer not null primary key autoincrement unique, 
        title text unique
        );

    create table Member(
        user_id integer,
        course_id integer,
        role integer,
        primary key(user_id, course_id)
        );

    create table Role(
        id integer, 
        title text unique
        );
""")

file = open("roster_data_sample.json").read()
data = json.loads(file)

#i;[0]name[1]course[2]role(in binary because the role in the json is 0,1)
for i in data:

    name = i[0]
    title = i[1]
    role = i[2]

    cur.execute("insert or ignore into User (name) values (?)", (name, ))
    cur.execute("select id from User where name = ?", (name, ))
    user_id = cur.fetchone()[0]

    cur.execute("insert or ignore into Course (title) values (?)", (title, ))
    cur.execute("select id from Course where title = ?", (title, ))
    course_id = cur.fetchone()[0]

    cur.execute(
        "insert or replace into Member (user_id,course_id,role) values (?,?,?)",
        (user_id, course_id, role))
    conn.commit()

#note find something better
#role in strings
role_title = ("Student", "Teacher")
i = 0
for title in role_title:
    cur.execute("insert into Role (id,title) values (?,?)", (i, title))
    conn.commit()
    i += 1

#checking
for row in cur.execute(
        "select User.name, Role.title, Course.title from User join Member join Course join Role on User.id = Member.user_id and Member.course_id = Course.id and Role.id = Member.role order by Course.title, Role.title DESC, User.name"
):
    print(row[0], row[1], row[2])

cur.close()