# -*- coding:UTF-8 -*-
import psycopg2
import boto3
from bs4 import BeautifulSoup
from bostondate import bostondate

s3 = boto3.resource('s3')
# date = bostondate()
date = '2019-02-04'
object = s3.Object('animecrawling', date + '/all_anime.txt')
soup = BeautifulSoup(object.get()['Body'], "lxml")
li = soup.find_all('li', itemtype='http://schema.org/TVSeries')

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print("Opened database successfully")

for each in li:
    a_bf = BeautifulSoup(str(each), "lxml")
    a = a_bf.find('a')
    # print(each.get('group_id'), a.get('title'))
    # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
    insert_data = "INSERT INTO anime (a_id, a_title, a_url, a_date) VALUES (%s, %s, %s, %s) \
                    ON CONFLICT (a_id) DO NOTHING;  "

    data = (each.get('group_id'), each.a.get('title'), each.a.get('href'), date)
    try:
        cur = conn.cursor()
        cur.execute(insert_data,data)
        conn.commit()
        # print("Records created successfully")
    except Exception as e:
        print('insert record into table failed')
        print(e)

    # finally:
    #     if cur:
    #         cur.close()

    # object_e = s3.Object('animecrawling', date + '/' + each.get('group_id') + '.txt')
    # soup_e = BeautifulSoup(object.get()['Body'], "lxml")
    # a1 = soup_e.find_all('a', "portrait-element block-link titlefix episode")
    # if a1.get('href') != str(row[2]):
    #     for string in a1.stripped_strings:
    #         info = str(string)
    #         break
    #     update_data = "UPDATE ANIMENAME\
    #                        SET lastupdated = %s, \
    #                              epinfo = %s,\
    #                               epurl = %s\
    #                        WHERE groupid = %s;"
    #
    #     data = (date, info, a1.get('href'), row[0])
    #     # try:
    #     cur = conn.cursor()
    #     cur.execute(update_data, data)
    #     # cur.execute("INSERT INTO ANIMENAME (GROUPID,NAME,URL) \
    #     #       VALUES ([" + each.get('group_id') + "],[" +  a.get('title') + "],[" + self.server + a.get('href') +"])");
    #
conn.commit()
conn.close()

print(len(li))



