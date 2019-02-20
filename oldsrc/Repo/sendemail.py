import psycopg2
# -*- coding:UTF-8 -*-
import time
import boto3
import botocore
import datetime
import pytz



def get_part_vendors(size):
    """ query part and vendor data from multiple tables"""
    conn = None
    date_format = '%Y-%m-%d'
    date = datetime.datetime.now(tz=pytz.utc)
    date1 = date.astimezone(pytz.timezone('US/Pacific')).strftime(date_format)
    print(date1)
    print(type(date1))
    try:
        conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        cur = conn.cursor()
        cur.execute("             SELECT name, epinfo, epurl \
            FROM animename \
            WHERE lastupdated >  DATE  %s - INTEGER '6'; \
         ", (date1,))
        print('bbbaaaa')
        # WHERE lastupdated >= DATE %s- INTEGER '6';
        # for row in iter_row(cur, 10):
        # for row in iter_1batchrow(cur, 5):
        #     print(row[1])
        # rows = cur.fetchmany(size)
        # print(rows[0][1])
        rows = cur.fetchall()
        print('aaaa')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows

if __name__ == '__main__':
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")
    size = 3
    rows = get_part_vendors(size)
    print(rows)
    # s3 = boto3.resource('s3')
    # date = time.strftime("%Y-%m-%d", time.localtime())
    # # for row in rows[]:
    # #     req = requests.get(url=row[1])
    # #     html = req.text
    # #     object = s3.Object('animecrawling', date + '/' + str(row[0])+'.txt')
    # #     object.put(Body=html)
    #
    # s3 = boto3.resource('s3')
    # for row in rows:
    #     try:
    #         s3.Object('animecrawling', date + '/' + str(row[0]) + '.txt').load()
    #     except botocore.exceptions.ClientError as e:
    #         if e.response['Error']['Code'] == "404":
    #             print('NO')
    #         else:
    #             # Something else has gone wrong.
    #             raise
    #     else:
    #         print('YES')# The object does exist.
    #
    #
