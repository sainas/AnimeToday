from bs4 import BeautifulSoup
import psycopg2

import time
import boto3


# def get_part_vendors():
""" query part and vendor data from multiple tables"""
conn = None
# try:
conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
cur = conn.cursor()
cur.execute("""
    SELECT groupid, url, epurl
    FROM animename;
""")
# for row in iter_row(cur, 10):
# for row in iter_1batchrow(cur, 5):
#     print(row[1])
rows = cur.fetchmany(5)

s3 = boto3.resource('s3')
date = time.strftime("%Y-%m-%d", time.localtime())
for row in rows:
    print(row)
    object = s3.Object('animecrawling', date + '/' + str(row[0]) + '.txt')
    bf = BeautifulSoup(object.get()['Body'], "lxml")
    a1 = bf.find('a', "portrait-element block-link titlefix episode")
    if a1.get('href') != str(row[2]):
        for string in a1.stripped_strings:
            info = str(string)
            break
        update_data = "UPDATE ANIMENAME\
                       SET lastupdated = %s, \
                             epinfo = %s,\
                              epurl = %s\
                       WHERE groupid = %s;"

        data = (date, info, a1.get('href'), row[0])
    # try:
        cur = conn.cursor()
        cur.execute(update_data, data)
        # cur.execute("INSERT INTO ANIMENAME (GROUPID,NAME,URL) \
        #       VALUES ([" + each.get('group_id') + "],[" +  a.get('title') + "],[" + self.server + a.get('href') +"])");
        conn.commit()
        print("Records created successfully")
    # print(a1.get('href'))
    # for string in a1.stripped_strings:
    #     print(string)

# print(rows[0][1])
# rows = cur.fetchall()
# cur.close()
# except (Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
cur.close()
if conn is not None:
    conn.close()
# return rows

# get_part_vendors()
# s3 = boto3.resource('s3')
# date = time.strftime("%Y-%m-%d", time.localtime())
# for row in rows:
#     object = s3.Object('animecrawling', date + '/' +str(row[0]) +'.txt')
#     bf = BeautifulSoup(object.get()['Body'], "lxml")
#     a1 = bf.find('a', "portrait-element block-link titlefix episode")
#     print(a1.get('href'))
#     for string in a1.stripped_strings:
#         print(string)

