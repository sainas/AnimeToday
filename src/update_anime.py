# -*- coding:UTF-8 -*-
import psycopg2
import boto3
from bs4 import BeautifulSoup

from bostondate import bostondate


def update_anime(date):
    s3 = boto3.resource('s3')
    object = s3.Object('animecrawling', date + '/all_anime.txt')
    soup = BeautifulSoup(object.get()['Body'], "lxml")
    li = soup.find_all('li', itemtype='http://schema.org/TVSeries')

    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print("Opened database successfully")

    for each in li:
        a_bf = BeautifulSoup(str(each), "lxml")
        a = a_bf.find('a')
        print(each.get('group_id'), a.get('title'))
        # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
        insert_data = "INSERT INTO anime (a_aid, a_atitle, a_aurl, a_adate) VALUES (%s, %s, %s, %s) \
                        ON CONFLICT (a_aid) DO NOTHING;  "

        data = (each.get('group_id'), each.a.get('title'), each.a.get('href'), date)
        try:
            cur = conn.cursor()
            cur.execute(insert_data,data)
            conn.commit()
            print("Records created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Update anime failed')
        finally:
            if cur:
                cur.close()

    conn.close()
    print('Finish', len(li))


if __name__ == '__main__':
    date = bostondate()
    update_anime(date)
