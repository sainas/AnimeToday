import psycopg2
import boto3

s3 = boto3.resource('s3')

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print("Opened database successfully")

cur = conn.cursor()
cur.execute("""
    SELECT full_title, ep_url, pub_date
    FROM episode
    WHERE pub_date IN ('2019-02-03' ,'2019-02-04');
""")
# for row in iter_row(cur, 10):
# for row in iter_1batchrow(cur, 5):
#     print(row[1])
rows = cur.fetchall()
print(rows[1])
