import psycopg2
conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print('connect to PostgreSQL success')
cur = conn.cursor()
cur.execute('''CREATE TABLE anime(
                 a_id        integer,
                 a_title     varchar(255) NOT NULL,
                 a_url       varchar(255) NOT NULL,
                 a_pic       varchar(2083),
                 PRIMARY KEY(a_id)
             );''')

cur.execute('''CREATE TABLE episode(
                 a_id       integer,
                 ep_id      integer,
                 ep_title   varchar(255) NOT NULL,
                 ep_url     varchar(2083),
                 pub_date    date,
                 PRIMARY KEY (ep_id),
                 FOREIGN KEY (a_id) REFERENCES anime(a_id)
             );''')

cur.execute('''CREATE TABLE userinfo(
                 username      varchar(20),
                 useremail     varchar(128),
                 PRIMARY KEY(username)
             );''')

cur.execute('''CREATE TABLE following(
                username      varchar(20),
                a_id        integer,
                FOREIGN KEY (username) REFERENCES userinfo(username),
                FOREIGN KEY (a_id) REFERENCES anime(a_id)
             );''')
conn.commit()
cur.close()
conn.close()

# cur.execute("ALTER TABLE ANIMENAME \
# ADD COLUMN lastupdated DATE NOT NULL DEFAULT to_date('2019-01-01','YYYY-MM-DD'),\
# ADD COLUMN epinfo TEXT, \
# ADD COLUMN epurl TEXT;")
# conn.commit()
# cur.close()
# conn.close()
