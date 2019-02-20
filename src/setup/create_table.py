# -*- coding:UTF-8 -*-
import psycopg2

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print('connect to PostgreSQL success')
cur = conn.cursor()


try:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE anime(
                     a_aid        integer,
                     a_atitle     varchar(255) NOT NULL,
                     a_aurl       varchar(255) NOT NULL,
                     a_aimg      varchar(2083),
                     a_adate     date,
                     PRIMARY KEY(a_id)
                 );''')

    cur.execute('''CREATE TABLE episode(
                     a_aid       integer,
                     e_epid      integer,
                     e_eptitle   varchar(255) NOT NULL,
                     e_eptitle2   varchar(255) ,
                     e_epurl     varchar(2083),
                     e_epdate    date,
                     PRIMARY KEY (e_epid),
                     FOREIGN KEY (a_aid) REFERENCES anime(a_aid)
                 );''')

    cur.execute('''CREATE TABLE userinfo(
                     u_username      varchar(20),
                     u_useremail     varchar(128),
                     PRIMARY KEY(u_username)
                 );''')

    cur.execute('''CREATE TABLE following(
                    f_username      varchar(20),
                    f_aid        integer,
                    FOREIGN KEY (f_username) REFERENCES userinfo(u_username),
                    FOREIGN KEY (f_aid) REFERENCES anime(a_aid)
                    UNIQUE (f_username, f_aid)
                 );''')

    conn.commit()
    print("Tables created successfully")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if cur:
        cur.close()

conn.close()
