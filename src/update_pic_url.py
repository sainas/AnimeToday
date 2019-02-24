# -*- coding:UTF-8 -*-
import psycopg2
import requests
from bs4 import BeautifulSoup


def where_pic_null():
    conn = None
    try:
        conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        cur = conn.cursor()
        cur.execute("""
            SELECT a_aid, a_aurl
            FROM anime
            WHERE a_aimg IS NULL;
        """)
        # rows = cur.fetchmany(6)
        rows = cur.fetchall()
        print('Success')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows


def update_pic_url(rows):
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    cur = conn.cursor()

    for each in rows:
        server = 'https://www.crunchyroll.com'
        myurl = server + each[1]
        req = requests.get(url=myurl)
        html = req.text
        soup = BeautifulSoup(html, "lxml")
        data = (soup.find('img', itemprop='image').get('src'), each[0])
        update_data = "UPDATE anime\
                       SET a_aimg = %s \
                       WHERE a_aid = %s;"
        try:
            cur = conn.cursor()
            cur.execute(update_data, data)
            conn.commit()
            print(each[0])
            print("Records created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Update image url failed')
        finally:
            if cur:
                cur.close()
    conn.close()


if __name__ == '__main__':
    rows = where_pic_null()
    update_pic_url(rows)





