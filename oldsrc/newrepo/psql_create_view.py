import psycopg2
conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print('connect to PostgreSQL success')
cur = conn.cursor()

#
# cur.execute('''CREATE TABLE anime(
#                  a_id        integer,
#                  a_title     varchar(255) NOT NULL,
#                  a_url       varchar(255) NOT NULL,
#                  a_pic       varchar(2083),
#                  PRIMARY KEY(a_id)
#              );''')

conn.commit()
cur.close()
conn.close()


