# -*- coding:UTF-8 -*-
import psycopg2
import boto3
from bs4 import BeautifulSoup
from bostondate import bostondate

def update_episode(date):
    s3 = boto3.resource('s3')
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")

    object = s3.Object('animecrawling', date + '/all_anime.txt')
    soup = BeautifulSoup(object.get()['Body'], "lxml")
    li = soup.find_all('li', itemtype='http://schema.org/TVSeries')
    i = 0
    for each in li:
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


            insert_data = '''INSERT INTO episode (e_aid, e_epid, e_eptitle1, e_eptitle2, e_epurl, e_epdate, e_epfulltitle) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s) 
                             ON CONFLICT (e_epid) DO NOTHING;  '''

            data = (filename, epid, eptitle, eptitle2, epurl, date, fulltitle)
            # print(date, fulltitle)
            try:
                cur = conn.cursor()
                cur.execute(insert_data,data)

                print("Records created successfully")
            except Exception as e:
                print('insert record into table failed')
                print(e)
        i = i+1
        print(i, filename)
    conn.commit()
    conn.close()

    print('finish')


date = bostondate()
for i in range(8):
    list = ['05','06','07','08','09','10','11','12']
    date = '2019-02-'+list[i]
    print(date)
    update_episode(date)