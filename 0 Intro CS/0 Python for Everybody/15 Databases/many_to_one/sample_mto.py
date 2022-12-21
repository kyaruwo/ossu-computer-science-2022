import sqlite3
import os

os.chdir("15 Databases/many_to_one")

conn = sqlite3.connect("sample_lms.sqlite")
cur = conn.cursor()

cur.executescript("""
    drop table if exists User;
    drop table if exists Course;
    drop table if exists Member;

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
""")

student = [("Jane", "jane@tsugi.org"), ("Ed", "ed@tsugi.org"),
           ("Sue", "sue@tsugi.org")]
course = ["Python", "SQL", "PHP"]

for name, email in student:
    print(name, email)
    cur.execute("insert into User (name, email) values (?,?)", (name, email))
    conn.commit()
for subject in course:
    print(subject)
    cur.execute("insert into Course (title) values (?)", (subject, ))
    conn.commit()

cur.executescript("""
    INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

    INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
    INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

    INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
    INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
""")
conn.commit()

cur.executescript("""
    drop table if exists Role;

    create table Role(
        title text unique,
        id integer
    );

    insert into Role (title, id) values ("teacher", 1);
    insert into Role (title, id) values ("student", 0);
""")
conn.commit()

for row in cur.execute(
        "SELECT User.name, Role.title, Course.title FROM User JOIN Member join Role JOIN Course ON Member.user_id = User.id AND Member.course_id = Course.id and Role.id = Member.role ORDER BY Course.title, Role.title DESC, User.name"
):
    print(row[0], row[1], row[2])

cur.close()