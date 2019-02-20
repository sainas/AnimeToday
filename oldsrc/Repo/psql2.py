import psycopg2
conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print('success')
cur = conn.cursor()
# cur.execute('''CREATE TABLE article (
#                  art_id      integer,
#                  title       varchar(128),
#                  content     text,
#                  author      varchar(128),
#                  pub_date    date,
#                  PRIMARY KEY(art_id)
#              );''')
# conn.commit()
#
cur.execute("ALTER TABLE ANIMENAME \
ADD COLUMN lastupdated DATE NOT NULL DEFAULT to_date('2019-01-01','YYYY-MM-DD'),\
ADD COLUMN epinfo TEXT, \
ADD COLUMN epurl TEXT;")
conn.commit()
cur.close()
conn.close()
