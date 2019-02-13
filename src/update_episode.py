# -*- coding:UTF-8 -*-
import psycopg2
import boto3
from bs4 import BeautifulSoup
from bostondate import bostondate

s3 = boto3.resource('s3')
# date = bostondate()
date = '2019-02-04'
conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
print("Opened database successfully")

object = s3.Object('animecrawling', date + '/all_anime.txt')
soup = BeautifulSoup(object.get()['Body'], "lxml")
li = soup.find_all('li', itemtype='http://schema.org/TVSeries')
i = 0
for each in li[600:]:
    filename = each.get('group_id')
    object = s3.Object('animecrawling', date + '/' + filename + '.txt')
    soup = BeautifulSoup(object.get()['Body'], "lxml")
    div = soup.find_all('div', 'wrapper container-shadow hover-classes')
    for eachep in div:
        epid = eachep.find_all('div', 'episode-progress')[0].get('media_id')
        eptitle = eachep.span.get_text().strip()
        eptitle2 = eachep.p.get_text().strip()
        epurl = eachep.a.get('href')
        fulltitle = eachep.a.get('title')


        insert_data = '''INSERT INTO episode (a_id, ep_id, ep_title, ep_title2, ep_url, pub_date, full_title) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s) 
                         ON CONFLICT (ep_id) DO NOTHING;  '''

        data = (filename, epid, eptitle, eptitle2, epurl, date, fulltitle)
        # print(date, fulltitle)
        try:
            cur = conn.cursor()
            cur.execute(insert_data,data)

            # print("Records created successfully")
        except Exception as e:
            print('insert record into table failed')
            print(e)
    i = i+1
    print(i, filename)
conn.commit()
conn.close()

print('finish')
