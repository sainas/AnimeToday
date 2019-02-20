# -*- coding: utf-8 -*-
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def application():
    try:
        conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        try:
            cur = conn.cursor()
            # cur.execute('''CREATE TABLE article (
            #                  art_id      integer,
            #                  title       varchar(128),
            #                  content     text,
            #                  author      varchar(128),
            #                  pub_date    date,
            #                  PRIMARY KEY(art_id)
            #              );''')
            # conn.commit()
        #
            cur = conn.cursor()
            cur.execute("ALTER TABLE ANIMENAME \
            ADD COLUMN lastupdated DATE NOT NULL DEFAULT to_date('2019-01-01','YYYY-MM-DD'),\
            ADD COLUMN epinfo TEXT, \
            ADD COLUMN epurl TEXT;")
            conn.commit()
        except psycopg2.OperationalError:
            output = 'sorry Fail！'
    except psycopg2.OperationalError:
        output = 'sorry Connection Fail！'
    else:
        output = 'Yeah！'
    finally:
        # cur.close()
        conn.close()
    # status = '200 OK'
    # response_headers = [('Content-type', 'text/html; charset=utf-8'),
    #                     ('Content-Length', str(len(output)))]
    # start_response(status, response_headers)

    return [output]

application()