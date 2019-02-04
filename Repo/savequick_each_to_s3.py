import psycopg2
# -*- coding:UTF-8 -*-
import requests
import time
import boto3
import boto3
import botocore




import psycopg2

# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


class GetAllAnimeName:

    def __init__(self):
        self.target = 'https://www.crunchyroll.com/videos/anime/alpha?group=all'
        self.server = 'https://www.crunchyroll.com'
        self.title = []
        self.urls = []
        self.nums = []

    def get_url(self):
        # conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        # print("Opened database successfully")


        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        li = bf.find_all('li', itemtype='http://schema.org/TVSeries')
        # for each in li:
        #     a_bf = BeautifulSoup(str(each), "lxml")
        #     a = a_bf.find('a')
        #     print(each.get('group_id'), a.get('title'))
        #     # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
        #     insert_data = "INSERT INTO ANIMENAME (GROUPID,NAME,URL) VALUES (%s, %s, %s) \
        #                     ON CONFLICT (GROUPID) DO UPDATE SET \
        #                     name = EXCLUDED.name,  \
        #                     url = EXCLUDED.url;  "
        #
        #     data = (each.get('group_id'), a.get('title'), self.server + a.get('href'))
        #     try:
        #         cur = conn.cursor()
        #         cur.execute(insert_data,data)
        #          # cur.execute("INSERT INTO ANIMENAME (GROUPID,NAME,URL) \
        #         #       VALUES ([" + each.get('group_id') + "],[" +  a.get('title') + "],[" + self.server + a.get('href') +"])");
        #         conn.commit()
        #         print("Records created successfully")
        #     except Exception as e:
        #         print('insert record into table failed')
        #         print(e)
        #
        #     finally:
        #         if cur:
        #             cur.close()
        #
        # conn.close()

        print(len(li))
        # print(type(a.get('title')))
        # for each2 in div：
        #     print(each2.get('class'))
        #     # a_bf = div_bf[0].find_all('a')
        return li

#
# if __name__ == '__main__':
#     test = GetAllAnimeName()
#     test.get_url()




# cur = conn.cursor()
# cur.execute('''CREATE TABLE ANIMENAME
#        (GROUPID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        URL            TEXT     NOT NULL);''')
# print("Table created successfully")

# conn.commit()
# conn.close()

# cur = conn.cursor()
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
#
# conn.commit()
# print("Records created successfully")
# conn.close()


#
# def iter_1batchrow(cursor, size=5):
#     for i in range(1):
#         rows = cursor.fetchmany(size)
#         if not rows:
#             break
#         for row in rows:
#             yield row

#
# def get_part_vendors(size):
#     """ query part and vendor data from multiple tables"""
#     conn = None
#     try:
#         conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
#         cur = conn.cursor()
#         cur.execute("""
#             SELECT groupid, url
#             FROM animename;
#         """)
#         # for row in iter_row(cur, 10):
#         # for row in iter_1batchrow(cur, 5):
#         #     print(row[1])
#         # rows = cur.fetchmany(size)
#         # print(rows[0][1])
#         rows = cur.fetchall()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#     return rows


if __name__ == '__main__':
    # conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    # print("Opened database successfully")
    # size = 3
    # rows = get_part_vendors(size)
    # print(len(rows))


    test = GetAllAnimeName()
    li = test.get_url()

    s3 = boto3.resource('s3')
    date = time.strftime("%Y-%m-%d", time.localtime())
    i = 290
    for each in li[290:]:
        a_bf = BeautifulSoup(str(each), "lxml")
        a = a_bf.find('a')
        print(each.get('group_id'), a.get('title'))
        # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
        # data = (each.get('group_id'), a.get('title'), self.server + a.get('href'))
        a_url = 'https://www.crunchyroll.com' + a.get('href')
        req = requests.get(url=a_url)
        html = req.text
        # print(html)
        object = s3.Object('animecrawling', date + '/' + each.get('group_id') + '.txt')
        object.put(Body=html)
        print(i)
        i = i+1
        time.sleep(1)

# Check if certain exist
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


