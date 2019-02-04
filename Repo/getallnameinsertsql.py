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
        conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
        print("Opened database successfully")


        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        li = bf.find_all('li', itemtype='http://schema.org/TVSeries')
        for each in li:
            a_bf = BeautifulSoup(str(each), "lxml")
            a = a_bf.find('a')
            print(each.get('group_id'), a.get('title'))
            # print(each.get('group_id'), a.get('title'), self.server + a.get('href'))
            insert_data = "INSERT INTO ANIMENAME (GROUPID,NAME,URL) VALUES (%s, %s, %s) \
                            ON CONFLICT (GROUPID) DO UPDATE SET \
                            name = EXCLUDED.name,  \
                            url = EXCLUDED.url;  "

            data = (each.get('group_id'), a.get('title'), self.server + a.get('href'))
            try:
                cur = conn.cursor()
                cur.execute(insert_data,data)
                 # cur.execute("INSERT INTO ANIMENAME (GROUPID,NAME,URL) \
                #       VALUES ([" + each.get('group_id') + "],[" +  a.get('title') + "],[" + self.server + a.get('href') +"])");
                conn.commit()
                print("Records created successfully")
            except Exception as e:
                print('insert record into table failed')
                print(e)

            finally:
                if cur:
                    cur.close()

        conn.close()

        print(len(li))
        print(type(a.get('title')))
        # for each2 in div：
        #     print(each2.get('class'))
        #     # a_bf = div_bf[0].find_all('a')


if __name__ == '__main__':
    test = GetAllAnimeName()
    test.get_url()




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


